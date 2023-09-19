from django.shortcuts import render,HttpResponse
from .models import Songs
import json

from django.views.generic import TemplateView

class SongpageView(TemplateView):
	template_name = 'song.html'

def songlist(request):
	song=Songs.objects.all()
	return render(request,"song.html",{'song':song})

# def api(request):
# 	data={"name":"ayush",
# 		"age":12,
# 		"address":"Bafal",
# 		}
# 	json_object = json.dumps(data) 
# 	return HttpResponse(json_object)
# # 	print(json_object)

# # data={"name":"ayush",
# # 		"age":12,
# # 		"address":"Bafal",
# # 		}
# # json_object = json.dumps(data) 
# # dict_obj=json.loads(json_object)
# # # print(dict_obj['name'])
# print(json_object['name'])

