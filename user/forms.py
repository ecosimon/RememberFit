#user/forms.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Need to redo this, a custom login is needed. research authentication
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
							  
							  
class SignUpForm(forms.Form):
    """
	    Default sign up form for our custom registration. Testing is required.
    """
    username = forms.CharField(max_length=30, blank=True)
    emmail = forms.CharField(max_length=255, blank=True)
	
    def clean_username(self):
        """
            Clean method is called when .is_valid() is invoked. This checks if the current username is taken in auth_user.
        """
        cd_username = self.cleaned_data.get('username')

        if not cd_username:
            raise forms.ValidationError('You need a username in order to sign up!')
        if (User.objects.get(username=cd_username).count() > 0):
            raise forms.ValidationError('This user is already taken!')
        return cd_username
		
    def clean_email(self):
        """
            Clean method is called when .is_valid() is invoked. Checks if the current email is in use.
        """
        cd_email = self.cleaned_data.get('email')
		
        if not cd_email:
            raise forms.ValidationError('Email is required for sign up!')
        if (User.objects.get(email=cd_email).count() > 0):
            raise forms.ValidationError('This email is already taken!')
        return cd_email
		

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