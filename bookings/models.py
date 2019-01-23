from datetime import date

from django.db import models

from locations.models import Location


class Booking(models.Model):
    rent = models.PositiveIntegerField(default=200)
    created_at = models.DateField(default=date.today)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='bookings')
