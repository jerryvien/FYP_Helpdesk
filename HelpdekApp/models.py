from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from mongoengine.django.auth import User
from mongoengine import *
from messagekey import *
import datetime
import os

# Create your models here.

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class RegisterUser(Document):
    userName = StringField(max_length=10, required=True)
    display_name = StringField(max_length=10, required=True)
    email = EmailField(required=True)
    password = StringField(min_length=6, max_length=12,required=True)
    confirm_password = StringField(min_length=6, max_length=12,required=True)

class CustomUser(User):
    address = StringField()

#class Admin(Document):
 #   userName = StringField(max_length=10, required=True)
  #  eMail = EmailField(required=True)
   # password = StringField(min_length=6, max_length=12,required=True)
    #confirmPassword = StringField(min_length=6, max_length=12,required=True)
    #ticket = ListField(ReferenceField(RegisterUser))

