from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {
        "message":"Listado de productos",
        "products":[
            {'title': "Playera", "Precio":"$5", "stock":True},
            {'title': "Camisa", "Precio":"$7", "stock":True},
            {'title': "Mochila", "Precio":"$20", "stock":False},
        ]
        })