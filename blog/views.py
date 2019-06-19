from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

#home
def home(request):
    return render(request, 'home.html')

#post list
def explore(request):
    blogs = Blog.objects
    return render(request, 'main.html', {'blogs': blogs})

#post detail view
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

#post create form
def new(request):
    return render(request, 'usercreate.html')

#form action; views.new 
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    
    return redirect('/blog/' + str(blog.id))

# photos
def photos(request):
    return render(request, 'photos.html')

