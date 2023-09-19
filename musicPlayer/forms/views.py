from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def login(request):
	form=LoginForm()
	return render(request,'login.html',{"form":form})