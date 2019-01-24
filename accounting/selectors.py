from datetime import date, timedelta

from django.contrib.auth.models import User

from locations.models import Location
from accounting.models import Payment, Invoice, CreditNote, Refund
from bookings.models import Booking

from permissions.services import check_entity_permission
from permissions.constants import EntityConstants


def get_sales_report(*, location: Location, user: User) -> dict:
    check_entity_permission(
        entity=EntityConstants.VIEW_SALES_REPORT,
        user=user,
        location=location
    )

    invoices = Invoice.objects.filter(booking__location=location).values_list('amount', flat=True)
    credit_notes = CreditNote.objects.filter(booking__location=location).values_list('amount', flat=True)
    payments = Payment.objects.filter(invoice__booking__location=location).values_list('amount', flat=True)
    refunds = Refund.objects.filter(credit_note__booking__location=location).values_list('amount', flat=True)

    report = {
        'invoices': sum(invoices),
        'credit_notes': sum(credit_notes),
        'payments': sum(payments),
        'refunds': sum(refunds)
    }

    arrivals = get_arrivals_for_sales_report(location=location)
    today_arrivals = arrivals.get(str(date.today()), [])

    return {'report': report, 'arrivals': sum(x['rent'] for x in today_arrivals)}


def get_arrivals_for_sales_report(*, location: Location) -> dict:
    """
    This selector is exactly the same as `bookings.selectors.get_arrivals`
    but doesn't perform permission checks.
    """
    arrival_dates = [
        date.today() - timedelta(days=1),
        date.today(),
        date.today() + timedelta(days=1)
    ]

    arrivals = Booking.objects.filter(created_at__in=arrival_dates, location=location)
    # Initializing the result
    result = {str(date): [] for date in arrival_dates}
    # Building the result
    for date_ in arrival_dates:
        for arrival in arrivals:
            if arrival.created_at == date_:
                result[str(date_)].append({
                    'id': arrival.id,
                    'rent': arrival.rent
                })

    return result
