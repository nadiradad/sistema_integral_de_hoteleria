from django.contrib import admin
from .models import Reserva

# Register your models here.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id_habitacion', 'id_servicio_adicional', 'estado')
    list_filter = ('estado', 'id_habitacion')      # filtros laterales
    search_fields = ('estado',) 