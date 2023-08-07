from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from library.models import Library

from clients.models import Client
from utils.decorators.form_validation import Request
from utils.decorators.method_allowed import method_allowed
from utils.exceptions import LinkExpiredException, ClientDuplicateException, InvalidUsernameException, \
    IncorrectPasswordException
from utils.response import HTTPResponseSuccess


@csrf_exempt
@method_allowed(['POST'])
@Request.body_validation(
    form=dict(
        username=dict(
            required=True,
            max_length=128,
            type=str,
            field_name='UserName'
        ),
        password=dict(
            required=True,
            max_length=128,
            type=str,
            field_name='password'
        ),
        firstName=dict(
            required=True,
            max_length=128,
            type=str,
            field_name='FirstName'
        ),
        lastName=dict(
            required=True,
            max_length=128,
            type=str,
            field_name='LastName'
        )
    )
)
def register(request, **kwargs):
    body = kwargs['body']
    username = body['password']
    first_name = body['FirstName']
    last_name = body['LastName']
    password = body['password']
    library = Library.objects.get_or_create()[0]
    new_client = Client.objects.create(

    )

