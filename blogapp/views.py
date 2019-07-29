from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Blog
# Create your views here.


def main(request):
    blogs = Blog.objects
    return render(request, 'post/main.html', {'blogs': blogs})


def detail(request, post_id):
    post_detail = get_object_or_404(Blog, pk=post_id)
    return render(request, 'post/detail.html', {'post': post_detail})


def new(request):
    return render(request, 'post/new.html')


def Create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blogapp/' + str(blog.id))
