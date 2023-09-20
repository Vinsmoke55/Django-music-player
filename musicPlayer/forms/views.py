from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

# Create your views here.
def login(request):
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			username=data['Username']
			return render(request,'index.html',{'username':username})

	else:
		form=LoginForm()
	return render(request,'login.html',{"form":form})
