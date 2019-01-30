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


def get_caller():
    import inspect

    stack = inspect.stack()
    # Here I am in the `__call__` of the instance
    caller_call_frame = stack[3].frame
    # This is the Caller instance that called `check_entity_permission`
    # *NOTE* If the funciton is not wrapped with `with_optional_permissions` the `caller_itself`
    # will not be a `Caller` instance (it'll most likely be the API that calls the selector)
    caller_itself = caller_call_frame.f_locals.get('self', None)

    print(f'The caller of the function: {caller_itself}')

    if not isinstance(caller_itself, Caller):
        return None

    return caller_itself
