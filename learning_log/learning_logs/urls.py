""" defined the url patterns for learning_logs """

#from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # index
    #    url(r'^$',view.index, name='index'),
    path('', views.index, name='index'),
    # show all theme
    path('topics/', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic'),
    # the web page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
]
