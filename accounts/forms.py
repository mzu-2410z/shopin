# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email', 'phone',
            'dob', 'gender', 'address_line1', 'city', 'state', 'zip_code',
            'password1', 'password2'
        )
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email', 'phone',
            'dob', 'gender', 'address_line1', 'city', 'state', 'zip_code'
        )


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            "placeholder": "you@example.com",
        })
    )
