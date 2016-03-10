from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.template import Context, loader
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from forms import *
from functions import *
from models import *
from messagekey import *
from bson import ObjectId
import json
import operator
from django.http import *
from django.shortcuts import  *
import datetime
import time
def index(request):
    form = LoginForm
    post = request.POST
    post._mutable = True
    # allow change data in request.POST
    user = User.objects.get(id=ObjectId("56cb0301dbaf600e7408158e"))
    #a = RegisterUser.objects.get(userName = 'abc')
    raise Http404("index.html")
    #User.create_user(username="Test", password='12345')

    if request.method == main_key.POST:
        form = LoginForm(post)
        account =  form.data['account']
        password =  form.data['password']

        if(account == "123"):
            return HttpResponse('ok')
    else:
        form = LoginForm()

    context = {
        'forms': form,
        'user': user
    }
    return render(request, 'index.html', context)

def logout_view(request):
    session = request.session
    title = 'Logout'
    user = GetUser(session['login_user'])
    system_log(user,title)
    logout(request)
    return HttpResponseRedirect(main_key.TO_LOGIN_PAGE)

def forget_password(request):
    title = main_key.RESET_PASSWORD_PAGE_TITLE
    form = ResetPasswordForm
    post = request.POST
    post._mutable = True
    if request.method == main_key.POST:
        form = ResetPasswordForm(post)
        if form.is_valid():
            account = form.data['account']
            user = GetUser(account)
            if user != False:
                #new_password = GenerateRandomPassword(user)
                user.set_password('Password123')
                user.save()
                return HttpResponseRedirect(main_key.TO_LOGIN_PAGE) # Redirect after POST
    else:
        form = ResetPasswordForm()

    context ={
        main_key.TEMPLATE_TITLE: title,
         'r_form': form,
     }
    return render(request, 'resetPassword.html', context)

def login_view(request):
    title = main_key.LOGIN_TITLE
    form = LoginForm
    r_form = ResetPasswordForm
    post = request.POST
    post._mutable = True
    session = request.session
    user = False
    if request.method == main_key.POST:
        form = LoginForm(post)
        if form.is_valid():
            account = form.data['account']
            password = form.data['password']
            user = GetUser(account)
            if user != False:
                session['login_user'] = user.username
                user.last_login = datetime.datetime.now();
                user.save()
                system_log(user,title)
                if user.is_superuser != True :
                    return HttpResponseRedirect(main_key.TO_USER_HOME_PAGE)
                else:
                    return HttpResponseRedirect(main_key.TO_HOME_PAGE)
    else:
        form = LoginForm()

    context = {
        main_key.TEMPLATE_TITLE: title,
        'forms': form,
    }
    return render(request, 'login.html', context)

def login_template(request):
    title = main_key.LOGIN_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,

    }
    return render(request, 'login_template.html', context)

def registration(request):

    form = RegisterForm
    post = request.POST
    post._mutable = True

    if request.method == main_key.POST:
        form = RegisterForm(post)
        if form.is_valid():
            username = form.data['username']
            display_name = form.data['display_name']
            email = form.data['email']
            password = form.data['password']
            address = form.data['address']
            contactNum = form.data['contact_number']
            #gender = form.data['gender']
            #User.create_user(username=username,password=password,email=email)
            user = CreateUser(username,password,email,display_name,address,contactNum)
            title = 'Register'
            system_log(user,title)
            #user = CustomUser.create_user(username=username,password=password,email=email)
            #user.address = address
            #user.save()

        return HttpResponseRedirect(main_key.TO_LOGIN_PAGE)
    else:
        form = RegisterForm() # An unbound form

    title = main_key.REGISTER_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,
        'forms': form,
    }
    return render(request, 'registration.html', context)

def error(request):
    return render(request, '404.html')

def validation(request):
    return render(request, 'form-validation.html')

def googleMap(request):
    return render(request, 'google-map.html')

def blank(request):
    title = main_key.BASE_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,
    }
    return render(request, 'main_template.html', context)

def test(request):

    title = main_key.DASHBOARD_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,

    }
    return render(request, 'test.html', context)

def dashboard(request):
    session = request.session

    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
        pass
    else:
        user = CustomUser.objects.get(username=session['login_user'])


    log = SystemLog.objects.all()

    title = main_key.DASHBOARD_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,
        'user': user,
        'log':log
    }
    return render(request, 'dashboard.html', context)

def agent_dashboard(request):
    session = request.session

    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
        pass
    else:
        user = CustomUser.objects.get(username=session['login_user'])


    log = SystemLog.objects.all()
    userR = CustomUser.objects.all()
    title = main_key.DASHBOARD_TITLE

    context = {
        main_key.TEMPLATE_TITLE: 'User '+title,
        'user': user,
        'userR': userR,
        'log':log
    }
    return render(request, 'agent_dashboard.html', context)

def user_dashboard(request):
    session = request.session

    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
        pass
    else:
        user = CustomUser.objects.get(username=session['login_user'])


    log = SystemLog.objects.all()
    userR = CustomUser.objects.all()
    title = main_key.DASHBOARD_TITLE

    context = {
        main_key.TEMPLATE_TITLE: 'User '+title,
        'user': user,
        'userR': userR,
        'log':log
    }
    return render(request, 'user_dashboard.html', context)

def user_directory(request):

    session = request.session
    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
    else:
        user = CustomUser.objects.get(username=session['login_user'])


    log = SystemLog.objects.all()
    userR = CustomUser.objects.all()

    title = 'User Directory'

    context = {
        main_key.TEMPLATE_TITLE: title,
        'user': user,
        'userR': userR,
        'log':log
    }
    return render(request, 'user_directory.html', context)

def ticket_directory(request):

    session = request.session
    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
    else:
        user = CustomUser.objects.get(username=session['login_user'])


    log = SystemLog.objects.all()
    userR = CustomUser.objects.all()
    title = 'Ticket Directory'
    context = {
        main_key.TEMPLATE_TITLE: title,
        'user': user,
        'userR': userR,
        'log':log
    }
    return render(request, 'ticket_directory.html', context)

def ticket_details(request,key):

    session = request.session
    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
    else:
        user = CustomUser.objects.get(username=session['login_user'])

    userR = CustomUser.objects.all()
    form = Create_Ticket_Form
    post = request.POST
    post._mutable = True

    if request.method == main_key.POST:
        form = Create_Ticket_Form(post)
        ticket = RequestDetails()
        log = LogDetails()
        ticket.last_change_date = datetime.datetime.now()
        ticket.request_type = form.data['request_type']
        ticket.impact = form.data['impact']
        ticket.urgency = form.data['urgency']
        ticket.status = form.data['status']
        ticket.team = form.data['team']
        for item in userR:
            for item2 in item.ticket:
                if item2.ticket_number == key:
                    item2.log.agent_id = user.username
                    item2.log_created_date = datetime.datetime.now()
                    item2.log.public_log = form.data['public_log']
                    item2.last_change_date = ticket.last_change_date
                    item2.request_type = ticket.request_type
                    item2.impact = ticket.impact
                    item2.urgency = ticket.urgency
                    item2.status = ticket.status
                    item2.team = ticket.team
                    item2.log.append(log)
                    item.save()
        return HttpResponseRedirect('/ticket_directory/')
    else:
        form = Create_Ticket_Form()

    for item in userR:
        for item2 in item.ticket:
            if item2.ticket_number == key:
                form.fields['request_type'].initial = item2.request_type
                form.fields['impact'].initial = item2.impact
                form.fields['urgency'].initial = item2.urgency
                form.fields['status'].initial = item2.status
                form.fields['team'].initial = item2.team


    log = SystemLog.objects.all()
    title = 'Ticket Directory'
    context = {
        main_key.TEMPLATE_TITLE: title,
        'user': user,
        'forms': form,
        'userR': userR,
        'ticket_id': key,
        'log':log
    }
    return render(request, 'ticket_details.html', context)

def user_ticket_details(request,key):

    session = request.session
    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
    else:
        user = CustomUser.objects.get(username=session['login_user'])


    log = SystemLog.objects.all()
    userR = CustomUser.objects.all()
    title = 'Ticket Detail'
    context = {
        main_key.TEMPLATE_TITLE: title,
        'user': user,
        'userR': userR,
        'ticket_id': key,
        'log':log
    }
    return render(request, 'user_ticket_details.html', context)

def create_ticket(request):
    session = request.session
    site =''
    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
    else:
        user = CustomUser.objects.get(username=session['login_user'])

    admin = GetAdmin(session['login_user'])
    requestor = GetUser(session['login_user'])
    if admin is False:
        site = 'user_create_ticket.html'
    else:
        site = 'create_ticket_admin.html'

    title = main_key.CREATE_TICKET_TITLE

    form = Create_Ticket_Form
    post = request.POST
    post._mutable = True


    if request.method == main_key.POST:
        form = Create_Ticket_Form(post)
        if form.is_valid():
            ticket = RequestDetails()
            ticket.created_date_time = datetime.datetime.now()
            ticket.ticket_number = 'T001'
            ticket.contact_number = form.data['contact']
            ticket.email = form.data['email']
            ticket.subject = form.data['subject']
            ticket.description = form.data['description']
            ticket.request_type = form.data['request_type']
            ticket.impact = form.data['impact']
            ticket.urgency = form.data['urgency']
            ticket.status = form.data['status']
            ticket.mode = form.data['mode']
            ticket.team = form.data['team']
            ticket.user = user.to_dbref()
            user.ticket.append(ticket)
            user.save()
            return HttpResponseRedirect(main_key.TO_HOME_PAGE)
    else:
        form = Create_Ticket_Form()

    context = {
        main_key.TEMPLATE_TITLE: title,
        'forms': form,
        'user': user
    }
    return render(request, 'create_ticket_admin.html', context)

def user_create_ticket(request):

    session = request.session
    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
    else:
        user = CustomUser.objects.get(username=session['login_user'])

    user2 = CustomUser.objects.get(username='Jerry')

    #admin = GetAdmin(session['login_user'])
    title = main_key.CREATE_TICKET_TITLE
    form = Create_Ticket_Form
    post = request.POST
    post._mutable = True
    #--fullname = request.POST["data1"]
    #--user.fullname = fullname
    if request.method == main_key.POST:
        form = Create_Ticket_Form(post)
        ticket = RequestDetails()
        log = LogDetails()
        ticket.created_date_time = datetime.datetime.now()
        ticket.last_change_date = datetime.datetime.now()
        log.agent_id = user2.username
        log.log_created_date = datetime.datetime.now()
        log.public_log = form.data['description']
        random_ticket_id = random_ticket()
        ticket.ticket_number = random_ticket_id
        ticket.contact_number = user.contact_number
        ticket.email = user.email
        subject = form.data['subject']
        ticket.subject = subject
        description = form.data['description']
        ticket.description = description
        ticket.request_type = form.data['request_type']
        ticket.impact = 'Low'
        ticket.urgency = form.data['urgency']
        ticket.status = 'Open'
        ticket.mode = 'Web Form'
        ticket.team = 'MIS'
        ticket.user = user.to_dbref()
        ticket.agent = user2.to_dbref()
        ticket.log.append(log)
        user.ticket.append(ticket)
        user.save()
        SendEmail(user,random_ticket_id,subject,description)
        system_log(user,title)
        return HttpResponseRedirect(main_key.TO_USER_HOME_PAGE)
        form = Create_Ticket_Form()

    context = {
        main_key.TEMPLATE_TITLE: title,
        'forms': form,
        'user': user
    }
    #--return HttpResponse(jsonify({"success": True}))
    return render(request, 'user_create_ticket.html', context)

def profile(request, key):
    session = request.session
    user = CustomUser.objects.get(id=key)
    form = Agent_assignForm
    post = request.POST
    post._mutable = True
    title = user.username + " " + main_key.PROFILE_TITLE
    if request.method == main_key.POST:
        form = Agent_assignForm(post)
        agent = AgentDetails()
        agent.department = form.data['department']
        agent.agent_status = 'Available'
        agent.agent_id = get_random_string(length=5)
        agent.user = user.to_dbref()
        user.agent.append(agent)
        user.save()
        title = 'Agent_assign'
        system_log(user,title)
        return HttpResponseRedirect(main_key.TO_HOME_PAGE)
        form = Agent_assignForm()
    context = {
        main_key.TEMPLATE_TITLE: title,
        'user': user,
        'forms': form,
        'keys' :key,
        'leng' : len(user.ticket)
    }
    return render(request, 'profile.html', context)

def setAdmin(request,key):
    user2 = CustomUser.objects.get(id=key)

    context = {
        main_key.TEMPLATE_TITLE: "Profile edit",
    }
    return render(request, 'profile_edit.html', context)

def profileEdit(request, key):

    session = request.session
    user = CustomUser.objects.get(username=session['login_user'])
    user2 = CustomUser.objects.get(id=key)
    userR = CustomUser.objects.all()
    form = ProfileEditForm
    post = request.POST
    post._mutable = True

    if request.method == main_key.POST:
        form = ProfileEditForm(post)
        display_name = form.data['display_name']
        email = form.data['email']
        password = ''
        address = form.data['address']
        contactNum = form.data['contact_number']
        user = UpdateUser(user2,password,email,display_name,address,contactNum)
    else:
        form = ProfileEditForm()  # An unbound form


    form.fields['display_name'].initial = user2.display_name
    form.fields['email'].initial = user2.email
    form.fields['address'].initial = user2.address
    form.fields['contact_number'].initial = user2.contact_number

    context = {
        main_key.TEMPLATE_TITLE: "Profile edit",
        'user': user,
        'user2': user2,
        'userR': userR,
        'forms': form,
        'keys' :key,
    }
    return render(request, 'profile_edit.html', context)

def edit_profile(request,id=None, template_name='edit_profile.html'):
    if id:
        user = get_object_or_404(CustomUser, pk=id)
        if user.username != request.username:
            return HttpResponseForbidden()
    else:
        user = CustomUser(user=request.username)

    form = RegisterForm(request.POST or None, instance=user)
    if request.POST:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(main_key.TO_ERROR_PAGE)

    return render_to_response(template_name,{
        'form': form,
    },context_instance=RequestContext(request))


def user_profile(request, key):

    session = request.session
    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
    else:
        user = CustomUser.objects.get(username=session['login_user'])
        #if user.is_superuser == True:

    title = user.username + "'s " + main_key.PROFILE_TITLE

    form = ProfileEditForm
    post = request.POST
    post._mutable = True

    if request.method == main_key.POST:
        form = ProfileEditForm(post)
        display_name = form.data['display_name']
        email = form.data['email']
        password = form.data['password']
        address = form.data['address']
        contactNum = form.data['contact_number']
        user = UpdateUser(user,password,email,display_name,address,contactNum)
        return HttpResponseRedirect(main_key.TO_USER_HOME_PAGE)
    else:
        form = ProfileEditForm()  # An unbound form


        form.fields['display_name'].initial = user.display_name
        form.fields['email'].initial = user.email
        form.fields['address'].initial = user.address
        form.fields['contact_number'].initial = user.contact_number
        form.fields['password'].initial = user.password

    context = {
        main_key.TEMPLATE_TITLE: title,
        'user': user,
        'forms': form,
        'keys' :key,
        'leng': len(user.ticket)
    }
    return render(request, 'user_profile.html', context)

#--this
@csrf_exempt
def set_superuser_ajax(request):
    post = request.POST
    post._mutable = True  # allow change data in request.POST
    session = request.session

    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
    else:
        user = CustomUser.objects.get(username=session['login_user'])

#--example
    #myName = post["myName"]
    data = CustomUser.objects.get(id=ObjectId(post["user"]))
    if data.is_superuser == False:
        data.is_superuser = True
        data.is_staff = False
        data.team = 'Test'
    else:
        data.is_superuser = False
        data.is_staff = True

    data.save()
    #-- here u can add more
    return HttpResponse(jsonify({'is_superuser': data.is_superuser,
                                 'test': data.is_staff}))

#--this just reuse like the HttpResponse only
def jsonify(object, fields=None, to_dict=False):
    '''Funcion utilitaria para convertir un query set a formato JSON'''
    try:
        import json
    except ImportError:
        import django.utils.simplejson as json

    out = []

    if type(object) not in [dict, list, tuple]:
        for i in object:
            tmp = {}
            if fields:
                for field in fields:
                    tmp[field] = unicode(i.__getattribute__(field))
            else:
                for attr, value in i.__dict__.iteritems():
                    tmp[attr] = value
            out.append(tmp)
    else:
        out = object

    if to_dict:
        return out
    else:
        return json.dumps(out)