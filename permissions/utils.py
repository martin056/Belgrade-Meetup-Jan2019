class Caller:
    def __init__(self, func, _skip_permission_checks=False):
        self.func = func
        self._skip_permission_checks = _skip_permission_checks

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def skip_permissions(self):
        return Caller(func=self.func, _skip_permission_checks=True)


def with_optional_permissions(func):
    caller = Caller(func)

    return caller
