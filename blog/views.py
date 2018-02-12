from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def posts(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'post_list.html', {'posts':posts,})


def post_detail(request, postid):
    post = Post.objects.get(id=postid)
    return render(request, 'post_detail.html', {'post': post,'user':request.user})


def new_post(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            author = request.user
            text = request.POST.get('text')
            title = request.POST.get('title')
            post = Post.objects.create(author=author,text=text,title=title)
            post.save()
            return redirect('/posts/')
        else:
            return render(request, 'post_add.html')
    else:
        return HttpResponseRedirect('/index/')


def index(request): 
    return render(request,'index.html')