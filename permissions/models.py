from django.db import models
from django.contrib.auth.models import User

from locations.models import Location

from permissions.constants import EntityConstants


class Team(models.Model):
    members = models.ManyToManyField(User, through='permissions.TeamMembership', related_name='teams')
    locations = models.ManyToManyField(Location, related_name='teams')
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'Team {self.name}'

    @property
    def has_location(self):
        return self.locations.exists()

    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(*args, **kwargs)


class TeamMembership(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_memberships')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_memberships')

    def __str__(self):
        return f'{self.member} in {self.team}'

    class Meta:
        unique_together = (('team', 'member'),)


class TeamPermission(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='permissions')
    entity = models.CharField(max_length=255, choices=EntityConstants.ENTITY_CHOICES)
    value = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.full_clean()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.entity} in {self.team}'

    class Meta:
        unique_together = (('team', 'entity'),)
