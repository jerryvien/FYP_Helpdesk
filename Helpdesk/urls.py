"""Helpdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', 'HelpdekApp.views.index', name='Home'),
    url(r'^login/', 'HelpdekApp.views.login_view', name='Login'),
    url(r'^login_template/', 'HelpdekApp.views.login_template', name='Login'),
    url(r'^registration/', 'HelpdekApp.views.registration', name='Registration'),
    url(r'^test/', 'HelpdekApp.views.test', name='Registration'),
    url(r'^dashboard/', 'HelpdekApp.views.dashboard', name='Dashboard'),
    url(r'^profile/', 'HelpdekApp.views.profile', name='Profile'),
    url(r'^base/', 'HelpdekApp.views.blank', name='base')
]