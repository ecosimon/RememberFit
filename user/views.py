from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

"""
   Documentation for user/views.py as follows:
   
   Function-Based-Views will be adhered throughout this project until further notice.
   
   AJAX/Graphs will be implemented soon.
"""

# login_required decorator requires view to be authenticated
@login_required(login_url="login/")
def home(request):
    """
    Default home page for users to land on after signing up or logging in.
    May switch over to Class-based-views in the future when more data stats are added.
    """
    return render(request, "home.html")
	
def register(request):
    """
    This function adheres to Django's built-in registration form. 
    If a POST method is submitted, the POST will be appended to the form 
    where the form validation occurs in form.is_valid().
    After registration, user will be redirected to Login page to login.
	Otherwise, form errors will be prompted and a empty form is sent back.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('rpassword')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
	
