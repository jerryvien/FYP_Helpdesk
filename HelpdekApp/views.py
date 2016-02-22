from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from mongoengine.django.auth import User
from messagekey import *
# use to run http request
from forms import *
from models import RegisterUser
# Create your views here.
main_key = MainMsg
from bson.objectid import ObjectId

def index(request):
    form = LoginForm
    post = request.POST
    post._mutable = True
    # allow change data in request.POST
    user = User.objects.get(id=ObjectId("56cb0301dbaf600e7408158e"))
    #a = RegisterUser.objects.get(userName = 'abc')
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

def login_view(request):
    title = main_key.LOGIN_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,

    }
    return render(request, 'login.html', context)

def login_template(request):
    title = main_key.LOGIN_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,

    }
    return render(request, 'login_template.html', context)

def registration(request):

    title = main_key.REGISTER_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,

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

    title = main_key.DASHBOARD_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,

    }
    return render(request, 'dashboard.html', context)

def profile(request):

    title = main_key.PROFILE_TITLE

    context = {
        main_key.TEMPLATE_TITLE: title,

    }
    return render(request, 'profile.html', context)
