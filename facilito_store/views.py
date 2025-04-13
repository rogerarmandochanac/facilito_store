from django.http import HttpResponse

def index(request):
    return HttpResponse('Hola desde el Archivo views.py')