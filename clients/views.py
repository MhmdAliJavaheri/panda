from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from utils.decorators.form_validation import Request

from utils.decorators.method_allowed import method_allowed
from django.views.decorators.csrf import csrf_exempt
from .models import Client
from .forms import ClientCreateForm

from utils.exceptions import LinkExpiredException, ClientDuplicateException, InvalidUsernameException, \
    IncorrectPasswordException
from utils.response import HTTPResponseSuccess
# Create your views here.


def show_user(request):
    query = Client.objects.all().order_by('username')

    form = ClientCreateForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = ClientCreateForm

    dict = {
        'query': query,
        'form': form,
    }

    return render(request, 'panel/index.html', dict)

# @csrf_exempt
# @method_allowed(['POST'])
# @Request.body_validation(
#     form=dict(


#         firstName=dict(
#             required=True,
#             max_length=128,
#             type=str,
#             field_name='first name'
#         ),
#         lastName=dict(
#             required=True,
#             max_length=128,
#             type=str,
#             field_name='last name'
#         ),
#         password=dict(
#             required=True,
#             max_length=128,
#             type=str,
#             field_name='password'
#         )
#     )
# )
# def enter_to_panel(request, **kwargs):
#     body = kwargs['body']
#     username = body['username']
#     first_name = body['firstName']
#     last_name = body['lastName']
#     password = body['password']
