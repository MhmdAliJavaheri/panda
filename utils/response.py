from typing import Any, Dict

from django.http import JsonResponse


class HTTPResponse:

    def __new__(cls, data: Any = {}, headers: Dict = {}) -> JsonResponse:
        return super(HTTPResponse, cls).__new__(cls).json(data, headers)

    def json(self, data: Any, headers: Dict) -> JsonResponse:
        """
        :returns: json response by optional data and headers
        """
        response = JsonResponse(
            status=self.status_code,
            data=data,
            safe=False
        )
        if headers:
            for key, value in headers.items():
                response[key] = value
        return response


class HTTPResponseSuccess(HTTPResponse):
    status_code: int = 200


class HTTPResponseCreated(HTTPResponse):
    status_code: int = 201


class HTTPResponseAccepted(HTTPResponse):
    status_code: int = 202


class HTTPResponseNoContent(HTTPResponse):
    status_code: int = 204


class HTTPResponseMultipleChoices(HTTPResponse):
    status_code: int = 300


class HTTPResponseMovedPermanently(HTTPResponse):
    status_code: int = 301


class HTTPResponseFound(HTTPResponse):
    status_code: int = 302


class HTTPResponseNotModified(HTTPResponse):
    status_code: int = 304


class HTTPResponseBadRequest(HTTPResponse):
    status_code: int = 400


class HTTPResponseUnauthorized(HTTPResponse):
    status_code: int = 401


class HTTPResponseForbidden(HTTPResponse):
    status_code: int = 403


class HTTPResponseNotFound(HTTPResponse):
    status_code: int = 404


class HTTPResponseMethodNotAllowed(HTTPResponse):
    status_code: int = 405


class HTTPResponseConflict(HTTPResponse):
    status_code: int = 409


class HTTPResponseTooManyRequests(HTTPResponse):
    status_code: int = 429


class HTTPResponseInternalServerError(HTTPResponse):
    status_code: int = 500


class HTTPResponseNotImplemented(HTTPResponse):
    status_code: int = 501


class HTTPResponseBadGateway(HTTPResponse):
    status_code: int = 502


class HTTPResponseServiceUnavailable(HTTPResponse):
    status_code: int = 503


class HTTPResponseGatewayTimeout(HTTPResponse):
    status_code: int = 504
