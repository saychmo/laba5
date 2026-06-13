from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput()
    )

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

from django.forms import ModelForm

class ProfileUserForm(ModelForm):

    class Meta:
        model = User

        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )