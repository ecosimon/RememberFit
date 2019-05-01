from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .models import UserProfile
from .forms import SignUpForm

"""
   Documentation for user/views.py as follows:
   
   Function-Based-Views will be adhered throughout this project until further notice.
   
   AJAX/Graphs will be implemented soon.
   
   Comments for feature branch sake.
"""

# login_required decorator requires view to be authenticated
@login_required(login_url="login/")
def home(request):
    """
    Default home page for users to land on after signing up or logging in.
    May switch over to Class-based-views in the future when more data stats are added.
    """
    return render(request, "home.html")
	
# def register(request):
    # """
    # This function adheres to Django's built-in registration form. 
    # If a POST method is submitted, the POST will be appended to the form 
    # where the form validation occurs in form.is_valid().
    # After registration, user will be redirected to Login page to login.
	# Otherwise, form errors will be prompted and a empty form is sent back.
    # """
    # if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
            # form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('rpassword')
            # return redirect('login')
    # else:
        # form = UserCreationForm()
    # return render(request, 'signup.html', {'form': form})
	

def signup(request):
    """
        Custom registration function. Requires SignUp.html page for testing.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_userprofile = UserProfile(user=new_user, username=new_user.username)
            new_userprofile.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, '', {'form': form})
            
            
            
            
# work in progress
# class LineChartJSONView(BaseLineChartView):
    # def get_labels(self):
        # return ["January", "February", "March", "April", "May", "June", "july"]
		
    # def get_providers(self):
        # return ["Central", "Eastside", "Westside"]

    # def get_data(self):
        # return [[75, 44, 92, 11, 44, 95, 35],
                # [41, 92, 18, 3, 73, 87, 92],
                # [87, 21, 94, 3, 90, 13, 65]]

				
# line_chart = TemplateView.as_view(template_name='home.html')
# line_chart_json = LineChartJSONView.as_view()
