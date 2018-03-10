from django.shortcuts import render

from .models import Topic
# Create your views here.

def index(request):
    """ learn the home page for your notes """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ show all themes """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)