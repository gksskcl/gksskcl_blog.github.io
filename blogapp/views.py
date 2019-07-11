from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .models import Comment


def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})


def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})



def new(request):
    return render(request, 'new.html')


def intro(request):
    return render(request, 'intro.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) 

def com(request):   
    com = Comment()
    com.comment = request.GET['comment']
    com.save()
    comments = Comment.objects
    return render(request, 'home.html', {'comments':comments})