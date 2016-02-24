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
    url(r'^$', 'HelpdekApp.views.login_view', name='Login'),
    url(r'^login/', 'HelpdekApp.views.login_view', name='Login'),
    url(r'^logout/', 'HelpdekApp.views.logout_view', name='Logout'),
    url(r'^create_ticket/', 'HelpdekApp.views.create_ticket', name='Create_Ticket'),
    url(r'^error/', 'HelpdekApp.views.error', name='error'),
    url(r'^registration/', 'HelpdekApp.views.registration', name='Registration'),
    url(r'^test/', 'HelpdekApp.views.test', name='Registration'),
    url(r'^dashboard/', 'HelpdekApp.views.dashboard', name='Dashboard'),
    url(r'^validation/', 'HelpdekApp.views.dashboard', name='Dashboard'),
    url(r'^googleMaps/', 'HelpdekApp.views.googleMap', name='googleMaps'),
    url(r'^profile/', 'HelpdekApp.views.profile', name='Profile'),
    url(r'^base/', 'HelpdekApp.views.blank', name='base'),
    url(r'^resetPassword/', 'HelpdekApp.views.forget_password', name='resetPassword')

]
