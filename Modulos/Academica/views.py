from django.shortcuts import redirect, render
from ProyectoUniversidad import settings
from django.core.mail import send_mail
from .models import Curso
from django.contrib import messages

# Create your views here.
def FormularioContacto(request):

    return render(request, "formulario.html")

def Contactar(request):

    if request.method == "POST":

        asunto = request.POST["textoAsunto"]
        mensaje = request.POST["textoMensaje"] + " / Email: " + request.POST["textoEmail"]
        emailEmisor = settings.EMAIL_HOST_USER
        emailReceptor = ["Nanopier@gmail.com"]
        send_mail(asunto, mensaje, emailEmisor, emailReceptor, fail_silently = False)

        return render(request, "contactoExitoso.html")
    
    return render(request, "formulario.html")

def home(request):

    Cursos = Curso.objects.all()

    messages.success(request, 'Cursos listados')

    return render(request, 'gestionCursos.html', {"cursos": Cursos})

def RegistroCupo(request):

    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCredito']

    curso = Curso.objects.create(codigo = codigo, nombre = nombre, creditos = creditos)

    messages.success(request, 'Curso registrado con éxito')

    return redirect('/')

def EliminarCurso(request, codigo):

    curso = Curso.objects.get(codigo=codigo)

    curso.delete()

    messages.success(request, 'Curso eliminado')

    return redirect('/')

def EdicionCurso(request, codigo):

    curso = Curso.objects.get(codigo=codigo)

    return render(request, "edicionCurso.html", {"curso": curso})

def EditarCurso(request):

    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCredito']

    curso = Curso.objects.get(codigo=codigo)

    curso.codigo = codigo
    curso.nombre = nombre
    curso.creditos = creditos

    curso.save()

    messages.success(request, 'Curso editado')

    return redirect('/')


