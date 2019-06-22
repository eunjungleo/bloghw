from django.shortcuts import render
from .models import Photo

def photos(request):
    photos = Photo.objects
    return render(request, 'photos.html', {'photos': photos})

def dogs(request):
    return render(request, 'dogs.html')

def about(request):
    return render(request, 'about.html')
