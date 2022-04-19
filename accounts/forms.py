from django.forms import (EmailField, EmailInput, CharField, PasswordInput, TextInput)
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

import re


class UserLoginForm(AuthenticationForm):
    username = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-control'}))
    password = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    name = CharField(label='Name', widget=TextInput(attrs={'class': 'form-control'}))
    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-control'}))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(label='Re-password', widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')
