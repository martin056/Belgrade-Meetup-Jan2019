from datetime import date, timedelta

from django.contrib.auth.models import User

from locations.models import Location
from bookings.models import Booking

from permissions.services import check_entity_permission
from permissions.constants import EntityConstants


def get_arrivals(*, location: Location, user: User=None) -> dict:
    """
    Returns Bookings info for the last three days
    """
    if user is not None:
        check_entity_permission(
            entity=EntityConstants.VIEW_ARRIVALS,
            user=user,
            location=location
        )

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
