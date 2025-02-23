from django.conf import settings
from django.shortcuts import (render,
                            redirect)
from django.contrib.auth import (authenticate,
                                login, 
                                logout)

from django.contrib import messages 

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