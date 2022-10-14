from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import get_user_model
from django.contrib import auth

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user = User()
        
        user.username = request.POST.get('username', '')
        user.phone = request.POST.get('phone', '')
        user.address = request.POST.get('address', '')
        
        user.set_password(request.POST.get('password', ''))
        
        user.save()
        
        return redirect('/login/')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/home')
        else:
            return render(request, 'login.html')
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/home')
        else:
            return render(request, 'login.html')

def home(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'home.html')
    else:
        return redirect('/login')