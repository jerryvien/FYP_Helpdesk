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
STATUS_CHOICES = (
    ('OPEN','Open'),
    ('CLOSE','Close'),
)

class RegisterUser(Document):
    userName = StringField(max_length=10, required=True)
    email = EmailField(required=True)
    password = StringField(min_length=6, max_length=12,required=True)
    confirm_password = StringField(min_length=6, max_length=12,required=True)

class CustomUser(User):
    address = StringField()
    display_name = StringField(max_length=10)
    #ticket = EmbeddedDocumentField(RequestDetails)
    #status = StringField(choices= STATUS_CHOICES)

class RequestDetails(EmbeddedDocument):
    status = StringField(choices= STATUS_CHOICES)
    category = StringField(choices= STATUS_CHOICES)
    subcategory = StringField(choices= STATUS_CHOICES)
    created_by = StringField(choices= STATUS_CHOICES)
    department = StringField(choices= STATUS_CHOICES)
    due_by = DateTimeField()
    last_update_time = DateTimeField()
    created_time = DateTimeField()
    technician = StringField(choices= STATUS_CHOICES)
    piriority = StringField(choices= STATUS_CHOICES)





#class Admin(Document):
 #   userName = StringField(max_length=10, required=True)
  #  eMail = EmailField(required=True)
   # password = StringField(min_length=6, max_length=12,required=True)
    #confirmPassword = StringField(min_length=6, max_length=12,required=True)
    #ticket = ListField(ReferenceField(RegisterUser))

