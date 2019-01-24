from permissions.exceptions import NoEntityPermissionException


def check_entity_permission(*, user, entity, location, caller=None) -> None:
    print('Caller: ', caller)
    if caller is not None and getattr(caller, '_skip_permission_checks', False):
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
