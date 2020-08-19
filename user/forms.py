#user/forms.py
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

# Not really sure if this is needed. This can be initialized manually from UserForm.
# note: while user signs up, they can add their info and after registering data updates graph.
# class UserProfileForm(forms.ModelForm):
#     class Meta():
#         model = UserProfile
#         fields = ('user',)
