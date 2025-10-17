from django.urls import path
from . import views

urlpatterns = [
    path('servicios/', views.listado_servicios, name='listado_servicios'),
]
