from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
# Create your views here.


def logout_view(request):
    """ the cancellation of the user """
    logout(request)
    #return HttpResponseRedirect(reverse('learning_logs:index'))
    #return render(request, HttpResponseRedirect(reverse('learning_logs:index')))
    return render(request, 'learning_logs/index.html')
