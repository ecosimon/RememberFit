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
							  
# class SignUpForm(UserCreationForm):
    # """
    # A Sign up form extending Django's built-in UserCreationForm.
    # """
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    # email = forms.EmailField(max_length=254, help_text="This is required.")
	
    # class Meta:
        # model = User
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
		
    # def save(self, commit=True):
        # user = super(SignUpForm, self).save(commit=False)
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        # user.email = self.cleaned_data['email']
        # if commit:
            # user.save()
        # return user