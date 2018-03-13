from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def logout_view(request):
    """ the cancellation of the user """
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
    # must return render
    return render(request, 'learning_logs/index.html')


def register(request):
    """ register new user """
    if request.method != 'POST':
        # the empty registration form is displayed
        form = UserCreationForm()
    else:
        # process the completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # let the user login automatically and redirect to the home page
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
