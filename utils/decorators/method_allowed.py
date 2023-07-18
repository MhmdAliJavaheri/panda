from typing import Dict

from utils.response import HTTPResponseMethodNotAllowed


def method_allowed(verbs):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.method not in verbs:
                data: Dict = dict(
                    code=4051,
                    message=f'only {verbs} methods are allowed'
                )
                return HTTPResponseMethodNotAllowed(data=data)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator
