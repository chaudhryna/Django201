from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image',]
        