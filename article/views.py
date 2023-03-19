from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import AddArticleForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def homeview(request):
    posts = Post.objects.all()
    return render(request,'article/home.html',{'posts':posts})

def detailview(request, pk):
    post = get_object_or_404(Post,id=pk)
    return render(request,'article/detail.html',{'post':post})

def articlelist(request):
    posts = Post.objects.filter(author =request.user)
    return render(request,'article/list.html',{'posts':posts})

def addarticle(request):
    form = AddArticleForm()
    if request.method == 'POST':
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author=request.user
            obj.save()
            messages.success(request,'Article added.')
            return redirect('article:home')
    return render(request,'article/add.html',{'form':form})

def updatearticle(request,pk):
    post = get_object_or_404(Post,id=pk)
    form = AddArticleForm(instance=post)
    if request.method == 'POST':
        form = AddArticleForm( request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
            messages.success(request,'Article updated.')
            return redirect('article:list')
    return render(request,'article/update.html',{'form':form})

def deletearticle(request, pk):
    post = get_object_or_404(Post,id=pk)
    post.delete()
    messages.success(request,'Article removed.')
    return redirect('article:list')


def addcomment(request):
    if request.method == 'POST':
        text = request.POST.get('comment')
        id = request.POST.get('postid')
        post = get_object_or_404(Post,id=id)
        Comment.objects.create(user=request.user, text =text, post = post)
        messages.success(request,'Comment Posted.')
    return redirect(request.META.get('HTTP_REFERER'))

def removecomment(request,pk):
    comment = get_object_or_404(Comment,id=pk)
    comment.delete()
    messages.success(request,'Comment removed.')
    return redirect(request.META.get('HTTP_REFERER'))


def updatecomment(request):
    if request.method == 'POST':
        text = request.POST.get('comment')
        id = request.POST.get('commentid')
        obj = Comment.objects.get(id=id)
        obj.text = text
        obj.save()
        messages.success(request,'Comment Updated.')
    return redirect(request.META.get('HTTP_REFERER'))