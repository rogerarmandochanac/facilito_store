from django.conf import settings
from django.shortcuts import (render,
                            redirect)
from django.contrib.auth import (authenticate,
                                login, 
                                logout)

from django.contrib import messages

from .form import RegisterForm

from django.contrib.auth.models import User

from django import forms

def index_view(request):
    return render(request, 'index.html', {})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Usuario auntenticado correctamente.")
            return redirect("index")
    return render(request, 'users/login.html', {})

def logout_view(request):
    logout(request)
    messages.error(request, "Session cerrado con exito")
    return redirect("login")

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        if form.save():
            messages.success(request, "Usuario creado exitosamente")
            return redirect("index")
    return render(request, "users/register.html", {'form':form})