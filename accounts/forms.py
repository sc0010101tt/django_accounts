from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    username = forms.CharField(max_length=150, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
