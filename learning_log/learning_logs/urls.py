""" defined the url patterns for learning_logs """

#from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # index
#    url(r'^$',view.index, name='index'),
    path('', views.index,name='index')
]