from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def loginview(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login in success.')
            return redirect('/articles')
            
        else:
            messages.error(request, 'Account does not exist.')
    return render(request, 'account/login.html', context={'form': form})

def registerview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account successfully created.')
            return redirect('account:login')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})








