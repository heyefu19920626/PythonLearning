""" defined the url patterns for learning_logs """

#from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # index
#    url(r'^$',view.index, name='index'),
    path('', views.index,name='index'),
    # show all theme
    path('topics/', views.topics, name='topics'),
    path('^topics/(?P<topic_id>\d+)/$', views.topic,name='topic')
]