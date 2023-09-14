from django.shortcuts import render
from .models import Songs


from django.views.generic import TemplateView

# class SongpageView(TemplateView):
# 	template_name = 'song.html'

def songlist(request):
	song=Songs.objects.all()
	return render(request,"song.html",{'song':song})
