from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegistroForm, LoginForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # recuerda cambiar esto por la URL de inicio del app

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect('home')
    else:
        form = RegistroForm()
    
    return render(request, 'usuarios/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # url de inicio del app

    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('home')  # url de inicio del app

    return render(request, 'usuarios/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect('login')