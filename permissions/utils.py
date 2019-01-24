class Caller:
    def __init__(self, func, bind, _skip_permission_checks=False):
        self.func = func
        self.bind = bind
        self._skip_permission_checks = _skip_permission_checks

    def __call__(self, *args, **kwargs):
        if self.bind:
            return self.func(self, *args, **kwargs)

        return self.func(*args, **kwargs)

    def skip_permissions(self):
        return Caller(func=self.func, bind=self.bind, _skip_permission_checks=True)


def with_optional_permissions(*, bind: bool=False):
    def wrapper(f):
        caller = Caller(f, bind=bind)

        return caller
    return wrapper
