""" defined the url pattern for application user """

#from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import login

from . import views

app_name = 'users'

urlpatterns = [
    # login page
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
]
