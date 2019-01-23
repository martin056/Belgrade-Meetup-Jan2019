from django.contrib.auth.models import User

from locations.models import Location

from permissions.constants import Entity
from permissions.exceptions import NoEntityPermissionException


def check_entity_permission(*, user: User, entity: Entity, location: Location) -> None:
    if user.is_superuser:
        return

    has_permission = user.teams\
        .filter(
            permissions__entity=entity.value,
            permissions__value=True,
            locations__id__contains=location.id
        )\
        .exists()

    if not has_permission:
        raise NoEntityPermissionException()
