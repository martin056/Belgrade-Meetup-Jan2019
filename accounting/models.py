from django.db import models

from bookings.models import Booking


class Invoice(models.Model):
    amount = models.PositiveIntegerField()
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, related_name='invoices')

    def __str__(self):
        return f'{self.amount}$'


class Payment(models.Model):
    amount = models.PositiveIntegerField()
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, related_name='payments')


class CreditNote(models.Model):
    amount = models.PositiveIntegerField()
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, related_name='credit_notes')


class Refund(models.Model):
    amount = models.PositiveIntegerField()
    credit_note = models.ForeignKey(CreditNote, on_delete=models.SET_NULL, null=True, related_name='refunds')
