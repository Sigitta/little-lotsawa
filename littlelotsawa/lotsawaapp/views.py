from django.shortcuts import render
from .forms import UserForm, SearchForm, ProfileForm
from django.http import HttpResponseRedirect
from .models import MyUser
from django.contrib.auth.views import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def myhome(request):
    if request.user.is_authenticated():
        # Is the account active? It could have been disabled.
        # redirect, or however you want to get to the main view
        return redirect('/profile/')
    else:
        return login(request, template_name="base.html")

def about(request):
    return render(request, 'about.html')

@login_required
def baseloggedin(request):
    return render(request, 'baseloggedin.html')

def communitydetails(request):
    return render(request, 'communitydetails.html')


def dictionarydetails(request):
    return render(request, 'dictionarydetails.html')

@login_required
def edit(request):
    user = request.user
    if request.method == "POST":
        profile = ProfileForm(request.POST)
        if profile.is_valid():
            user.first_name = profile.cleaned_data['firstname']
            user.last_name = profile.cleaned_data['lastname']
            user.skype = profile.cleaned_data['skype']
            user.skill = profile.cleaned_data['skill']
            user.email = profile.cleaned_data['email']
            user.searching = profile.cleaned_data['searching']
            user.save()
            return redirect ('/')
    else:
        profile = ProfileForm(initial={'skype': user.skype, 'interests':  user.interests, 'skill': user.skill, 'email': user.email, 'searching': user.searching})
    return render(request, 'edit.html', {'profile':profile})


def lessondetails(request):
    return render(request, 'lessondetails.html')

def logoutsite(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    user = request.user
    if request.method == "GET":
        searchfield = SearchForm()
        trainees = user.show_trainingpartners()
    return render(request, 'profile.html', {'searchfield':searchfield, 'trainees':trainees})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            MyUser.objects.create_user(**form.cleaned_data)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('')
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})
