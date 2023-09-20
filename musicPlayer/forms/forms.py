from django import forms
from django.forms import PasswordInput

class LoginForm(forms.Form):
	Username = forms.CharField(label="Username", max_length=15)
	Email=forms.EmailField(label="Email")
	Password=forms.CharField(label="Password",widget=PasswordInput())