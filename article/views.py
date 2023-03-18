from django.shortcuts import render, get_object_or_404
from .models import Post
def homeview(request):
    posts = Post.objects.all()
    return render(request,'article/home.html',{'posts':posts})

def detailview(request, pk):
    post = get_object_or_404(Post,id=pk)
    return render(request,'article/detail.html',{'post':post})
