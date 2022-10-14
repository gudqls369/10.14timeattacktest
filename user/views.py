from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import get_user_model
from django.contrib import auth

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)

        new_user = User()
        new_user.username = username
        new_user.password = password
        new_user.phone = phone
        new_user.address = address
        new_user.save()
        return redirect('/login')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

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