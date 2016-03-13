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
    url(r'^user_create_ticket/', 'HelpdekApp.views.user_create_ticket', name='Create_Ticket_User'),
    url(r'^create_ticket/', 'HelpdekApp.views.create_ticket', name='Create_Ticket_Admin'),
    url(r'^user_directory/', 'HelpdekApp.views.user_directory', name='User Directory'),
    url(r'^ticket_directory/', 'HelpdekApp.views.ticket_directory', name='Ticket Directory'),
    url(r'^error/', 'HelpdekApp.views.error', name='error'),
    url(r'^registration/', 'HelpdekApp.views.registration', name='Registration'),
    url(r'^test/', 'HelpdekApp.views.test', name='Registration'),
    url(r'^dashboard/', 'HelpdekApp.views.dashboard', name='Dashboard'),
    url(r'^user_dashboard/', 'HelpdekApp.views.user_dashboard', name='User Dashboard'),
    url(r'^agent_dashboard/', 'HelpdekApp.views.agent_dashboard', name='Agent Dashboard'),
    url(r'^validation/', 'HelpdekApp.views.dashboard', name='Dashboard'),
    url(r'^googleMaps/', 'HelpdekApp.views.googleMap', name='googleMaps'),
    url(r'^profile/(?P<key>.+)/', 'HelpdekApp.views.profile', name='Profile'),
    url(r'^profile_edit/(?P<key>.+)/', 'HelpdekApp.views.profileEdit', name='Profile Edit'),
    url(r'^edit_profile/(?P<id>.+)/', 'HelpdekApp.views.edit_profile', name='Edit Profile'),
    url(r'^ticket_details/(?P<key>.+)/', 'HelpdekApp.views.ticket_details', name='Ticket Details'),
    url(r'^user_ticket_details/(?P<key>.+)/', 'HelpdekApp.views.user_ticket_details', name='Ticket Details'),
    url(r'^user_profile/(?P<key>.+)/', 'HelpdekApp.views.user_profile', name='User Profile'),
    url(r'^base/', 'HelpdekApp.views.blank', name='base'),
    url(r'^resetPassword/', 'HelpdekApp.views.forget_password', name='resetPassword'),
    url(r'^leave_application/', 'HelpdekApp.views.leave_application', name='LeaveApply'),
    url(r'^calander/', 'HelpdekApp.views.calander', name='calander'),
    url(r'^leave_list/', 'HelpdekApp.views.leave_list', name='LeaveList'),
    url(r'^get_calender/', 'HelpdekApp.views.get_calender', name='LeaveList'),
    url(r'^get_leave_calender/', 'HelpdekApp.views.get_leave_calender', name='LeaveList'),
    #--this
    url(r'^set_superuser_ajax/', 'HelpdekApp.views.set_superuser_ajax', name='Set SuperUser ajax'),
    url(r'^set_leave_ajax/', 'HelpdekApp.views.set_leave_ajax', name='Set Leave ajax'),
    #--url(r'^edit_profile_ajax/', 'HelpdekApp.views.edit_profile_ajax', name='base'),

]
