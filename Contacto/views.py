from django.shortcuts import redirect, render

from .forms import FormularioContacto

from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("Nombre")
            email = request.POST.get("Email")
            mensaje = request.POST.get("Mensaje")


            email = EmailMessage("Mensaje desde Web Music.All", 
            "El usuario {}, con direccion {}, escribe:\n\n {}".format(nombre, email, mensaje),
            "",["proyectodjango.music.all@gmail.com"], reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")

            except:
                return redirect("/contacto/?novalido")




    return render(request, "contacto/conatacto.html", {'miFormulario': formulario_contacto})

