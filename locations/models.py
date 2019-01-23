from django.db import models


class Location(models.Model):
    ref = models.CharField(max_length=10)
