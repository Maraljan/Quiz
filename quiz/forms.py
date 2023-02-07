from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import ModelForm

from .models import CustomUser, QuizModel


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm, AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class Quizform(ModelForm):
    class Meta:
        model = QuizModel
        fields = "__all__"
