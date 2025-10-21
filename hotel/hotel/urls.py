"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.habitacion import views
from apps.reserva import views as vista_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar_habitaciones/', views.listar_habitaciones, name='listar_habitaciones'),
    path('listar_reservas/', vista_reserva.listar_reservas, name='listar_reservas')
]
