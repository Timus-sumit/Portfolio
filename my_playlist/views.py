from django.shortcuts import render
from .models import My_playlist, Latest

# Create your views here.
def myplaylist(request):
    latest= Latest.objects
    playlist= My_playlist.objects
    return render(request ,'myplaylist/playlist.html',{'playlist':playlist,'latest':latest})
