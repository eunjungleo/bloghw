from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Blog, Guest

#home
def home(request):
    return render(request, 'home.html')

#post list
def texts(request):
    blogs = Blog.objects
    return render(request, 'texts.html', {'blogs': blogs})

#post detail view
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'texts_detail.html', {'blog': blog_detail})

# guests posts list
def friends(request):
    guests = Guest.objects
    return render(request, 'guests.html', {'guests': guests})

# post create form
def fromguests(request):
    return render(request, 'fromguests.html')

def fromguests_detail(request, guest_id):
    guest_detail = get_object_or_404(Guest, pk=guest_id)
    return render(request, 'guests_detail.html', {'guest': guest_detail})

#form action; views.new 
def fromguests_createform(request):
    guest = Guest()
    guest.title = request.GET['title']
    guest.body = request.GET['body']
    guest.pub_date = timezone.datetime.now()
    guest.save()
    
    return redirect('/blog/guests/' + str(guest.id))





