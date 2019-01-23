from datetime import date

from django.contrib.auth.models import User

from locations.models import Location
from accounting.models import Payment, Invoice, CreditNote, Refund
from bookings.selectors import get_arrivals

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

    arrivals = get_arrivals(location=location, user=user)
    today_arrivals = arrivals.get(str(date.today()), [])

    return {'report': report, 'arrivals': sum(x['rent'] for x in today_arrivals)}
