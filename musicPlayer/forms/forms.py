from django import forms

class LoginForm(forms.Form):
	Username = forms.CharField(label="Username", max_length=15)
	Email=forms.EmailField(label="Email")
	Password=forms.CharField(label="Password")