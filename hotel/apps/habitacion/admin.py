from django.contrib import admin

# Register your models here.
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'precio', 'disponible')
    list_filter = ('tipo', 'disponible')
    search_fields = ('numero',)
