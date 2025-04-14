from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request, 'index.html', {
        "message":"Listado de productos",
        "products":[
            {'title': "Playera", "Precio":"$5", "stock":True},
            {'title': "Camisa", "Precio":"$7", "stock":True},
            {'title': "Mochila", "Precio":"$20", "stock":False},
        ]
        })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            messages.success(request, "Bienvenido")
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuario o contraseña no validos")
    
    return render(request, 'users/login.html', {})