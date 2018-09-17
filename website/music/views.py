from django.shortcuts import render,get_object_or_404
from .models import Album
# Create your views here.
def index(request):
	albums = Album.objects.all()
	return render(request,'music/index.html',{'albums':albums})

def detail(request, pk):
	album = get_object_or_404(Album,pk=pk)
	return render(request,'music/detail.html',{'album':album})