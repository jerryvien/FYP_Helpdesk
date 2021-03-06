__author__ = 'Yee.Ch'


from mongoengine import *

class MainMsg(Document):

    COMPANY_TITLE = 'J&D Helpdesk Solutions'
    BASE_TITLE = 'J&D Helpdesk'
    LOGIN_TITLE = 'Login'
    REGISTER_TITLE = 'Registration'
    DASHBOARD_TITLE = 'Dashboard'
    CREATE_TICKET_TITLE = 'Request Details'
    PROFILE_TITLE = 'Profile'
    TEMPLATE_TITLE = 'template_title'
    HELPDESK_TITLE = 'J&D Helpdesk'
    LOGIN_PAGE_TITLE = 'Login'
    RESET_PASSWORD_PAGE_TITLE = 'Reset Password'
    REGISTER_PAGE_TITLE = 'Registration'
    POST = 'POST'
    TEMPLATE_TITLE = 'template_title'
    SUCCESS_ = 'success'
    FORM = 'form'
    CURRENT_PAGE = '/'
    TO_LOGIN_PAGE = '/login/'
    TO_HOME_PAGE = '/dashboard/'
    TO_USER_HOME_PAGE = '/user_dashboard/'
    LEAVE_APPLICATION_TITLE = 'Leave Apply'
    LEAVELIST_TITLE = 'Leave List'
    LEAVEEDIT_TITLE = 'Leave Edit'
    TO_ACTIVATE_PAGE = '/activate/'
    TO_ERROR_PAGE = '/error/'
    TO_REGISTER_PAGE = '/register/'
    LOGIN_PAGE = 'login.html'
    REGISTER_PAGE = 'register.html'
    CURRENT_DATE_TIME = 'current_datetime'
    TITLE = 'title'
    EMAIL_PATH = "/Email.txt"
    LEAVE_EMAIL_PATH = "/LeaveEmail.txt"
    REQUIRED = 'required'
    CLASS = 'class'
    PLACEHOLDER = 'placeholder'
    AUTOFOCUS = 'autofocus'
    ONFOCUS = 'onfocus'
    CURSORTOEND = 'this.value = this.value'
    STYLE = 'style'
    FORM_CONTROL_CLASS = 'form-control'
    FORM_CONTROL_CLASS_BUTTON ='form-control form-control-inline input-medium default-date-picker'
    BORDER_RED = 'border-color:red;'
    UNKNOWN_ERROR = 'Unknown error'