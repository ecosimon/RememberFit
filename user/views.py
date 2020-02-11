from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .models import UserProfile
from .forms import UserProfileForm
# from .forms import SignUpForm

# login_required decorator requires view to be authenticated
# @login_required(login_url="login/")
def home(request):
    """
    Default home page for users to land on after signing up or logging in.
    May switch over to Class-based-views in the future when more data stats are added.
    """
    return render(request, "home.html")
