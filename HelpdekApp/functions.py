__author__ = 'Yee.Ch'

from messagekey import *
from models import *
from django.core.mail import send_mail,BadHeaderError
from django.template import Context, Template
from Helpdesk import settings
import hashlib
import random


main_key = MainMsg


def CreateUser(username, password, email, display_name, address):
    user = CustomUser.create_user(username=username,
                                  password=password,
                                email=email)

    user.display_name = display_name
    user.last_login = datetime.datetime.now()
    user.date_joined = datetime.datetime.now()
    user.address = address
    user.save()
    return user

def GetUser(input_name):
    try:
        user = CustomUser.objects.get(username=input_name)
        return user
    except DoesNotExist:
            return False
    except Exception, e:
            return False

def CheckIsLoggedIn(request):
    if 'login_user' not in request:
        return False
    else:
        return True