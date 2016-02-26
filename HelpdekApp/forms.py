__author__ = 'Yee.Ch'
from django import forms
from django.forms import ModelForm
from HelpdekApp.models import RegisterUser
from models import *
from functions import *
from messagekey import *
from mongoengine.queryset import DoesNotExist
from djangotoolbox.fields import *

main_key = MainMsg

class LoginForm(forms.Form):
    account = forms.CharField(error_messages={main_key.REQUIRED: 'Username and password is required'},widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'Username',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))

    password = forms.CharField(error_messages={main_key.REQUIRED: 'Username and password is required'},widget=forms.PasswordInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                               main_key.PLACEHOLDER: 'Password'}))
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        account = cleaned_data.get('account')
        password = cleaned_data.get('password')

    def clean_account(self):
        data = self.data
        errors = self.add_error
        input = 'account'
        input2 = 'password'
        user = GetUser(data[input])
        if user is False:
            errors(input, 'Invalid Account or Password.')
        elif user.check_password(data[input2]) is False:
            errors(input, 'Invalid Account or Password.')

    def is_valid(self):
        ret = forms.Form.is_valid(self)
        for f in self.errors:
            self.fields[f].widget.attrs.update({main_key.STYLE: main_key.BORDER_RED})
        return ret


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=5,widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'Username',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS: main_key.CURSORTOEND}))

    display_name = forms.CharField(widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,'id': 'display_name',
                                                           main_key.PLACEHOLDER: 'Nickname',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))

    #gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS_BUTTON}), choices=(('M', 'Male'),('F', 'Female'),), initial=(('M', 'Male'),('F', 'Female')[0][0]))

    email = forms.EmailField(widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'E-Mail',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))

    address = forms.CharField(widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,'id': 'address',
                                                           main_key.PLACEHOLDER: 'Address',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS: main_key.CURSORTOEND}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,'id': 'password',
                                                               main_key.PLACEHOLDER:'Password'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,'id': 'confirm_password',
                                                               main_key.PLACEHOLDER:'Re-type Password'}))

    #status = forms.ChoiceField(choices= STATUS_CHOICES, label="",initial="",widget=forms.Select(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS}))

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get('username')
        display_name = cleaned_data.get('display_name')
        address = cleaned_data.get('address')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')


class ResetPasswordForm(forms.Form):
    account = forms.CharField(error_messages={main_key.REQUIRED: 'Username is required'},widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'Username',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))
    def clean(self):
        cleaned_data = super(ResetPasswordForm, self).clean()
        account = cleaned_data.get('account')

    def clean_account(self):
        data = self.data
        fields = self.fields
        errors = self.add_error
        input = 'account'

        user = GetUser(data[input])
        if user is False:
            errors(input, 'Invalid Username.')

class Create_Ticket_Form(forms.Form):
    description = forms.CharField(widget=forms.Textarea(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'Description',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))
    subject = forms.CharField(widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'Subject',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))
    contact = forms.CharField(widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'Contact',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))
    email = forms.CharField(widget=forms.TextInput(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS,
                                                           main_key.PLACEHOLDER: 'E-mail',
                                                           main_key.AUTOFOCUS: True,
                                                           main_key.ONFOCUS : main_key.CURSORTOEND}))

    status = forms.ChoiceField(choices= STATUS_CHOICES,widget=forms.Select(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS}))
    request_type = forms.ChoiceField(choices= REQUEST_CHOICES,widget=forms.Select(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS}))
    impact = forms.ChoiceField(choices=IMPACT_CHOICES,widget=forms.Select(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS}))
    urgency = forms.ChoiceField(choices= URGENCY_CHOICES,widget=forms.Select(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS}))
    mode = forms.ChoiceField(choices= MODE_CHOICES,widget=forms.Select(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS}))
    team = forms.ChoiceField(choices= TEAM_CHOICES,widget=forms.Select(attrs={main_key.CLASS: main_key.FORM_CONTROL_CLASS}))


    def clean(self):
         cleaned_data = super(Create_Ticket_Form, self).clean()
         subject = cleaned_data.get('subject')
         contact = cleaned_data.get('contact')
         email = cleaned_data.get('email')
         desctiption = cleaned_data.get('description')
         status= cleaned_data.get('status')
         request_type = cleaned_data.get('request_type')
         impact= cleaned_data.get('impact')
         urgency= cleaned_data.get('urgency')
         mode = cleaned_data.get('mode')
         team = cleaned_data.get('team')


    def clean_desctiption(self):
            data = self.data
            fields = self.fields
            errors = self.add_error
            input = 'description'




