__author__ = 'Yee.Ch'
from django import forms
from django.forms import ModelForm
from HelpdekApp.models import RegisterUser
from models import *
from messagekey import *
from mongoengine.queryset import DoesNotExist

main_key = MainMsg

class LoginForm(forms.Form):
    account = forms.CharField(widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: '123',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                               main_key.PLACEHOLDER: '456'}))





