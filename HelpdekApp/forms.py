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
                                                           main_key.PLACEHOLDER: 'Username',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                               main_key.PLACEHOLDER: 'Password'}))
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        account = cleaned_data.get('account')
        password = cleaned_data.get('password')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=5,widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'Username',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS: main_key.CURSORTOEND}))

    display_name = forms.CharField(widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'Display Name',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))

    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS_BUTTON}), choices=(('M', 'Male'),('F', 'Female'),), initial=(('M', 'Male'),('F', 'Female')[0][0]))

    email = forms.EmailField(widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'E-Mail',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                               main_key.PLACEHOLDER:'Password'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                               main_key.PLACEHOLDER:'Re-type Password'}))

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')



