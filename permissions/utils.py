from contextlib import contextmanager


def with_permissions(func):
    def wrapper(*args, **kwargs):
        func._skip_permission_checks = False

        return func(*args, **kwargs)
    return wrapper


@contextmanager
def skip_permissions(func):
    func._skip_permission_checks = True

    yield func

    func._skip_permission_checks = False
