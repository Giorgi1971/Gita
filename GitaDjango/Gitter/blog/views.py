import imp
from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'list':posts})



def user_page(request, pk):
    posts = Post.objects.filter(author__pk=pk)
    print(posts)
    return render(request, 'blog/user_page.html', {'posts':posts})
