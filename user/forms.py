#user/forms.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    """
    This form extends AuthenticationForm which is a Django feature for authenticating credentials.
	
    Fields:
        username - CharField which takes in text, max_length 30
        password - CharField which takes in text, max_length 30
    """
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
							  