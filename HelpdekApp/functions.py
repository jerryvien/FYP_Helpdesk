__author__ = 'Yee.Ch'

from messagekey import *
from models import *
from django.utils.crypto import get_random_string
from django.core.mail import send_mail,BadHeaderError
from django.template import Context, Template
from Helpdesk import settings
import hashlib
import random


main_key = MainMsg


def CreateUser(username, password, email, display_name, address, contactNum):
    user = CustomUser.create_user(username=username,
                                  password=password,
                                email=email)

    user.display_name = display_name
    user.last_login = datetime.datetime.now()
    user.date_joined = datetime.datetime.now()
    user.address = address
    user.contact_number = contactNum
    user.team = "Customer"
    user.status = "Available"
    user.agent_id = get_random_string(length=5)
    user.is_superuser = False
    user.is_staff = False
    user.save()
    return user

def UpdateUser(user,password, email, display_name, address, contactNum):

    user.email=email
    user.display_name = display_name
    user.address = address
    user.contact_number = contactNum
    user.save()
    return True

def GetUser(input_name):
    try:
        user = CustomUser.objects.get(username=input_name)
        return user
    except DoesNotExist:
            return False
    except Exception, e:
            return False

def GetAdmin(input_name):
    try:
        user = CustomUser.objects.get(username=input_name)
        if user.is_superuser == True:
            return True
        else:
            return False
    except DoesNotExist:
            return False
    except Exception, e:
            return False

def CheckIsLoggedIn(request):
    if 'login_user' not in request:
        return False
    else:
        return True

def system_log(user,title):
    log = SystemLog()
    if title == main_key.LOGIN_PAGE_TITLE:
        log.content = user.username+' has log In successfully'
        log.user = user.to_dbref()
        log.role = 'Admin'
        log.created_date_time = datetime.datetime.now()
        log.save()
    if title == 'Logout':
        log.content = user.username+' has log out successfully'
        log.user = user.to_dbref()
        log.role = 'Admin'
        log.created_date_time = datetime.datetime.now()
        log.save()
    if title == 'Register':
        log.content = user.username+' had just register as a member successfully'
        log.user = user.to_dbref()
        log.role = 'Admin'
        log.created_date_time = datetime.datetime.now()
        log.save()
    if title == main_key.CREATE_TICKET_TITLE:
        log.content = user.username+' had just create a ticket successfully'
        log.user = user.to_dbref()
        log.role = 'Admin'
        log.created_date_time = datetime.datetime.now()
        log.save()
    if title == 'Agent_assign':
        log.content = user.username+' has been promoted to agent'
        log.user = user.to_dbref()
        log.role = 'Admin'
        log.created_date_time = datetime.datetime.now()
        log.save()

def random_ticket():
    ticket_id = get_random_string(length=10)
    return ticket_id

def SendEmail(user,random_ticket_id,subject,description):
    email_path = main_key.EMAIL_PATH
    email_subject = "Ticket "+ random_ticket_id +" successfully created."
    email_sender = main_key.HELPDESK_TITLE + '<no-reply@'+main_key.HELPDESK_TITLE+'.com>'
    link = 'http://127.0.0.1:9002/user_ticket_details/'+random_ticket_id
    c=Context({'ticket_link': link,
               main_key.CURRENT_DATE_TIME: datetime.datetime.now(),
               'ticket_subject': subject})
    f = open(settings.MEDIA_ROOT + email_path, 'r')
    t = Template(f.read()) # read txt file
    f.close()
    message = t.render(c)
    try:
        send_mail(email_subject, message, email_sender, [user.email],fail_silently=False)
        return True
    except BadHeaderError:
        return False
