from django.shortcuts import render

# Create your views here.
def vista_principal(request):
    return render(request, 'pagina_principal.html')