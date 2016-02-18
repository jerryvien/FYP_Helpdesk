__author__ = 'Yee.Ch'


from mongoengine import *

class MainMsg(Document):

    COMPANY_TITLE = 'J&D Helpdesk Solutions'
    BASE_TITLE = 'J&D Helpdesk'
    LOGIN_TITLE = 'Login'
    REGISTER_TITLE = 'Registration'
    DASHBOARD_TITLE = 'Dashboard'
    PROFILE_TITLE = 'Profile'
    TEMPLATE_TITLE = 'template_title'