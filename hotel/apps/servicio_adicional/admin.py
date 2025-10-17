from django.contrib import admin
from .models import Servicio_adicional

# Personalización del admin de Servicio_adicional
@admin.register(Servicio_adicional)
class ServicioAdicionalAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion', 'costo')  # columnas visibles
    search_fields = ('codigo', 'nombre')                         # barra de búsqueda
    list_editable = ('nombre', 'descripcion', 'costo')            # campos editables desde la lista

