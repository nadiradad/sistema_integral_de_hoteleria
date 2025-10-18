from django.shortcuts import render
from .models import Reserva

# Create your views here.
def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reserva_list.html', {'reservas': reservas})