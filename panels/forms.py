from django import forms
from .models import *


class DataInput(forms.DateInput):
    input_type = 'date'


class AutherCreateForm(forms.ModelForm):
    class Meta:
        model = Auther
        fields = ('first_name', 'last_name', 'nick_name')


class PublisherCreateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'phone_number', 'location')


class BookCreateForm(forms.ModelForm):

    publish_year = forms.DateField(widget=DataInput)

    class Meta:
        model = Book
        fields = ('title', 'pages', 'summery', 'publish_year',
                  'auther', 'publisher')
