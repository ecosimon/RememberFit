from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .models import UserProfile
from .forms import UserForm
# from .forms import SignUpForm

# login_required decorator requires view to be authenticated
# @login_required(login_url="login/")
def home(request):
    """
    Default home page for users to land on after signing up or logging in.
    May switch over to Class-based-views in the future when more data stats are added.
    """
    return render(request, "home.html")

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_profile = UserProfile.objects.create(user=user)
            user_profile.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'signup.html', {})
