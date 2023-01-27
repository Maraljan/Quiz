from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm, AuthenticationForm):
    username = forms.CharField(label='Email / Username')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

