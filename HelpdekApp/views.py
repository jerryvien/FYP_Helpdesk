from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import get_object_or_404
from mongoengine.django.auth import User
from messagekey import *
# use to run http request
from django.contrib.auth import logout
from forms import *
from functions import *
from models import *
from messagekey import *
# Create your views here.
main_key = MainMsg
from bson.objectid import ObjectId
from django.http import Http404

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
            #gender = form.data['gender']
            #User.create_user(username=username,password=password,email=email)
            user = CreateUser(username,password,email,display_name,address)
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

    title = main_key.DASHBOARD_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,
        'user': user
    }
    return render(request, 'dashboard.html', context)

def create_ticket(request):
    session = request.session
    site =''
    if CheckIsLoggedIn(session) == False:
        return HttpResponseRedirect(main_key.TO_ERROR_PAGE) # Redirect after POST
    else:
        user = CustomUser.objects.get(username=session['login_user'])

    admin = GetAdmin(session['login_user'])

    if admin is False:
        site = 'create_ticket.html'
    else:
        site = 'create_ticket_admin.html'

    title = main_key.CREATE_TICKET_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,
        'user': user
    }
    return render(request, site, context)

def profile(request):

    title = main_key.PROFILE_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,

    }
    return render(request, 'profile.html', context)
