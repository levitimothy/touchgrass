from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator


def home(request):
    post = Post.objects.all()
    username = request.GET.get('username')
    if username != '' and username is not None:
        post = post.filter(username__icontains=username)
    newpost = post[::-1]
    paginator = Paginator(newpost, 5)
    page = request.GET.get('page')
    newpost = paginator.get_page(page)
    return render(request, 'touchgrass/home.html', {'post': newpost})


def newpost(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tg:home')
    return render(request, 'touchgrass/newpost.html', {'form': form})