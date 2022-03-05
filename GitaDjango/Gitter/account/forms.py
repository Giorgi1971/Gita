from django import forms
from .models import Author
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class AuthorForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta():
        model = Author
        exclude = ('user',)