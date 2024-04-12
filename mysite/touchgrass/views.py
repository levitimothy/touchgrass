from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


def home(request):
    post = Post.objects.all()
    newpost = post[::-1]
    return render(request, 'touchgrass/home.html', {'post': newpost})


def newpost(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tg:home')
    return render(request, 'touchgrass/newpost.html', {'form': form})