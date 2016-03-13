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
    ('Open','Open'),
    ('Close','Close'),
    ('On hold','On Hold'),
    ('Postpone','Postpone')

)
URGENCY_CHOICES = (
    ('High','High'),
    ('Normal','Normal'),
    ('Medium','Medium'),
    ('Low','Low')

)
IMPACT_CHOICES = (
    ('High','High'),
    ('Normal','Normal'),
    ('Medium','Medium'),
    ('Low','Low')

)
MODE_CHOICES = (
    ('Web Form','Web Form'),
    ('Phone','Phone'),
    ('Call','Call'),
    ('Instant Messaging','Instant Messaging')

)
TEAM_CHOICES = (
    ('MIS','MIS'),
    ('System Admin','System Admin'),
    ('Network Admin','Network Admin'),
    ('Cloud Admin','Cloud Admin')

)
REQUEST_CHOICES = (
    ('Upgrade/Service','Upgrade/Service'),
    ('Repair/Maintenance','Repair/Maintenance'),
    ('New Request','New Request')
)

LEAVE_CHOICE = (
    ('Medical Leave', 'Medical Leave'),
    ('Emergency Leave', 'Emergency Leave'),
    ('Paternity Leave', 'Paternity Leave'),
    ('Unpaid Leave', 'Unpaid Leave')
)
AGENT_CHOICE = (
    ('Admin', 'Admin'),
    ('Jerry', 'Jerry')
)

class RegisterUser(Document):
    userName = StringField(max_length=10, required=True)
    email = EmailField(required=True)
    password = StringField(min_length=6, max_length=12,required=True)
    confirm_password = StringField(min_length=6, max_length=12,required=True)

class LogDetails(EmbeddedDocument):
    department = StringField()
    #user = ReferenceField('CustomerUser')
    public_log = StringField()
    agent_id = StringField()
    log_created_date = DateTimeField()

class Calendar(Document):
    calanderid = StringField()
    date = DateTimeField()
    ph = BooleanField()
    weekend = BooleanField()

class TextDic(Document):
    text = StringField()
    requestType = StringField()

class RequestDetails(EmbeddedDocument):
    user = ReferenceField('CustomUser')
    agent = ReferenceField('CustomUser')
    ticket_number = StringField()
    description = StringField()
    created_date_time = DateTimeField()
    last_change_date = DateTimeField()
    targeted_resolved_date = DateTimeField()
    last_resolved_date = DateTimeField()
    log = ListField(EmbeddedDocumentField(LogDetails))
    public_log = StringField()
    email = EmailField()
    contact_number = StringField()
    subject = StringField()
    request_type = StringField()
    status = StringField()
    impact = StringField()
    urgency = StringField()
    mode = StringField()
    team = StringField()

class LeaveRequest(EmbeddedDocument):
    user = ReferenceField('CustomUser')
    typeLeave = StringField()
    startDate = DateTimeField()
    endDate = DateTimeField()
    reason = StringField()
    status = StringField()
    leave_id = StringField()


class SystemLog(Document):
    user = ReferenceField('CustomUser')
    role = StringField()
    content = StringField()
    created_date_time = DateTimeField(default=datetime.datetime.now())

class CustomUser(User):
    address = StringField()
    contact_number = StringField(max_length=12)
    display_name = StringField(max_length=10)
    team = StringField()
    status = StringField()
    agent_id = StringField()

    #ticket = EmbeddedDocumentField(RequestDetails)
    ticket = ListField(EmbeddedDocumentField(RequestDetails))
    leave = ListField(EmbeddedDocumentField(LeaveRequest))
    #status = StringField(choices= STATUS_CHOICES)

class Calender(Document):
    id = StringField()
    name = StringField()




#class Admin(Document):
 #   userName = StringField(max_length=10, required=True)
  #  eMail = EmailField(required=True)
   # password = StringField(min_length=6, max_length=12,required=True)
    #confirmPassword = StringField(min_length=6, max_length=12,required=True)
    #ticket = ListField(ReferenceField(RegisterUser))

