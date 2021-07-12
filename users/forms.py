from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import EmailField
from .models import profile
class UserRegisterForm(UserCreationForm):
    email=EmailField()

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']

class ScanningForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['scan_image']



