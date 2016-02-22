__author__ = 'Yee.Ch'

from messagekey import *
from models import *
from django.core.mail import send_mail,BadHeaderError
from django.template import Context, Template
from Helpdesk import settings
import hashlib
import random


main_key = MainMsg