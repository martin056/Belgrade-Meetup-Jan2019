from rest_framework.exceptions import ValidationError


NO_ENTITY_PERMISSION_EXCEPTION = 'No entity permission.'


class NoEntityPermissionException(ValidationError):
    default_detail = NO_ENTITY_PERMISSION_EXCEPTION
