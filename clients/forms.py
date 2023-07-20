from .models import Client
from django import forms


class DataInput(forms.DateInput):
    input_type = 'date'


class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('username', 'first_name', 'last_name', 'password')
