from django.shortcuts import render
from .models import Servicio_adicional

def listado_servicios(request):
    servicios = Servicio_adicional.objects.all()
    return render(request, 'servicio_adicional.html', {'servicios': servicios})

