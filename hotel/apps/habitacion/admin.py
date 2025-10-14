from django.contrib import admin
from .models import TipoHabitacion, Habitacion

# Personalización del admin de TipoHabitacion
@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # columnas visibles
    search_fields = ('nombre',)               # barra de búsqueda

# Personalización del admin de Habitacion
@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'precio', 'disponible')
    list_filter = ('tipo', 'disponible')      # filtros laterales
    search_fields = ('numero',)
    list_editable = ('precio', 'disponible')  # puedes editar estos campos directamente desde la lista
    
