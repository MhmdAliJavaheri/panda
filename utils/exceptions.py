from typing import Dict
from django.http import JsonResponse
from utils.messages import *

from utils.response import (
    HTTPResponseBadRequest,
    HTTPResponseForbidden,
    HTTPResponseUnauthorized, HTTPResponseConflict, HTTPResponseNotFound
)


class InvalidFormException(HTTPResponseBadRequest):
    message: str = INVALID_FORM

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class NotProvideException(HTTPResponseBadRequest):
    message: str = None

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls, *args, **kwargs) -> JsonResponse:
        code: int = cls.code()
        if kwargs.get('message'):
            cls.message = kwargs['message']
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class FormTypeException(HTTPResponseBadRequest):
    message: str = None

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls, *args, **kwargs) -> JsonResponse:
        code: int = cls.code()
        if kwargs.get('message'):
            cls.message = kwargs['message']
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class FormLengthException(HTTPResponseBadRequest):
    message: str = None

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls, *args, **kwargs) -> JsonResponse:
        code: int = cls.code()
        if kwargs.get('message'):
            cls.message = kwargs['message']
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class FormValidationException(HTTPResponseBadRequest):
    message: str = None

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls, *args, **kwargs) -> JsonResponse:
        code: int = cls.code()
        if kwargs.get('message'):
            cls.message = kwargs['message']
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class InvalidRefreshTokenException(HTTPResponseUnauthorized):
    message: str = INVALID_REFRESH_TOKEN_ERROR

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class NBFRefreshTokenException(HTTPResponseForbidden):
    message: str = NBF_REFRESH_TOKEN_ERROR

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class InvalidAccessTokenException(HTTPResponseUnauthorized):
    message: str = INVALID_ACCESS_TOKEN_ERROR

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class JTIAccessTokenException(HTTPResponseUnauthorized):
    message: str = JTI_ACCESS_TOKEN_ERROR

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class ExpireAccessTokenException(HTTPResponseUnauthorized):
    message: str = EXP_TOKEN_ERROR

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class JTIRefreshTokenException(HTTPResponseUnauthorized):
    message: str = JTI_REFRESH_TOKEN_ERROR

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class OrganizationException(HTTPResponseUnauthorized):
    message: str = ORGANIZATION_ERROR

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class InvalidUsernameException(HTTPResponseUnauthorized):
    message: str = INVALID_USERNAME_EXCEPTION

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class InvalidPasswordException(HTTPResponseUnauthorized):
    message: str = INVALID_PASSWORD_EXCEPTION

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class NotFoundUserException(HTTPResponseUnauthorized):
    message: str = NOT_FOUND_USER_EXCEPTION

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class LinkExpiredException(HTTPResponseUnauthorized):  # 401? is true
    message: str = LINK_EXPIRED_EXCEPTION

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class ClientDuplicateException(HTTPResponseConflict):
    message: str = CLIENT_DUPLICATE_EXCEPTION

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class InvalidDateException(HTTPResponseBadRequest):
    message: str = INVALID_DATE_FORMAT

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls, *args, **kwargs) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class NotFoundTicketException(HTTPResponseNotFound):
    message: str = NOT_FOUND_TICKET

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls, *args, **kwargs) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class NotFoundMessageException(HTTPResponseNotFound):
    message: str = NOT_FOUND_DOCUMENT

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls, *args, **kwargs) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)


class IncorrectPasswordException(HTTPResponseUnauthorized):
    message: str = INCORRECT_PASSWORD_EXCEPTION

    @classmethod
    def code(cls) -> int:
        return sum([ord(i) for i in cls.__name__])

    def __new__(cls, *args, **kwargs) -> JsonResponse:
        code: int = cls.code()
        data: Dict = dict(code=code, message=cls.message)
        return super().__new__(cls, data=data)
