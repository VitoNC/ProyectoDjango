from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "ProyectoEv1App/inicio.html")




def tienda(request):
    return render(request, "ProyectoEv1App/tienda.html")






