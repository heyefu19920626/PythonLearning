from django.shortcuts import render

# Create your views here.

def index(request):
    """ learn the home page for your notes """
    return render(request, 'learning_logs/index.html')