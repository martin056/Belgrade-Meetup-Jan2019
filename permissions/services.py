from django.contrib.auth.models import User

from locations.models import Location

from permissions.constants import Entity
from permissions.exceptions import NoEntityPermissionException
from permissions.utils import Caller


def check_entity_permission(
    *,
    user: User,
    entity: Entity,
    location: Location,
) -> None:
    import inspect

    stack = inspect.stack()
    # Here I am in the `__call__` of the instance
    caller_call_frame = stack[2].frame
    # This is the Caller instance that called `check_entity_permission`
    # *NOTE* If the funciton is not wrapped with `with_optional_permissions` the `caller_itself`
    # will not be a `Caller` instance (it'll most likely be the API that calls the selector)
    caller_itself = caller_call_frame.f_locals.get('self', None)

    print(f'The caller of the function: {caller_itself}')

    if isinstance(caller_itself, Caller) and caller_itself._skip_permission_checks:
        return

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
