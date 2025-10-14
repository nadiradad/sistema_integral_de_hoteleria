from django.shortcuts import render
from .models import Habitacion

# Create your views here.
def listar_habitaciones(request):
    habitaciones = Habitacion.objects.select_related('tipo').all()
    return render(request, 'listar_habitaciones.html', {'habitaciones': habitaciones})
