from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ['message']

class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        def save(self, commit=True):
            User = super(NewUserForm, self).save(commit=False)
            if commit:
                User.save()
                return User
            
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'age', 'county']