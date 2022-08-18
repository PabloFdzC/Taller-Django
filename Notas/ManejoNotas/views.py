# Controlador
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
# Se necesita para manejar las notas en la base de datos
from .models import Nota
# Permite responder la peticion
from django.contrib import messages
# Nos ayuda a crear filtros complejos como el que está en
# la función de borrar_nota
from django.db.models import Q

from django.http import HttpResponse

# Si se está autenticado muestra la ventana de mis notas, sino lo manda
# a iniciar sesión
def mis_notas(peticion):
    if peticion.user.is_authenticated:
        return render(peticion, 'notas/mis-notas.html')
    else:
        return redirect('iniciar-sesion')

# Guarda la nota ya sea que la esté editando o creando, si la está editando
# se debe enviar el id de la nota
def guardar_nota(peticion):
    print("--------------------------------------")
    print(peticion.POST)
    print(peticion.body)
    print("--------------------------------------")
    if peticion.method == 'POST' and peticion.user.is_authenticated:
        # Se revisa si no tiene el campo del id
        nombre = peticion.POST.get('nombre')
        texto = peticion.POST.get('texto')
        if 'id' not in peticion.POST:
            # Si no lo tiene entonces se crea una nueva nota
            nota = Nota.objects.create(
                usuario=peticion.user,
                nombre=nombre,
                texto=texto
                )
            nota.save()
            messages.success(peticion, 'Nota guardada.')
            return redirect('mis-notas')
        else:
            # Si tiene el id entonces se modifica la nota que esté
            # en la base de datos
            id_nota = int(peticion.POST.get('id'))
            nota = Nota.objects.filter(pk=id_nota)
            # Como devuelve un set de objetos tenemos que agarrar solo
            # 1 que de todas formas solo es uno porque lo buscamos por
            # id
            nota = nota.first()
            nota.nombre = nombre
            nota.texto = texto
            nota.save()
            return redirect('mis-notas')
    raise PermissionDenied

# Borra una nota según el id
def borrar_nota(peticion):
    if peticion.method == 'POST' and peticion.user.is_authenticated:
        id = peticion.POST.get('id')
        # Con filter busca la nota que se quiere borrar (una que tenga el id de la nota
        # y el usuario actual) y con delete la borra

        nota = Nota.objects.get(Q(pk=id) & Q(usuario=peticion.user))
        nota.delete()
        messages.success(peticion, 'Nota borrada.')
        return redirect('mis-notas')
    raise PermissionDenied

# Muestra una lista con las notas del usuario
def ver_mis_notas(peticion):
    if peticion.method == 'GET' and peticion.user.is_authenticated:
        return render(peticion, 'notas/lista-notas.html',{
            'notas':Nota.objects.filter(usuario=peticion.user)
            })
    return HttpResponse(status=201)

def editar_nota(peticion):
    if peticion.method == 'GET' and peticion.user.is_authenticated:
        id = peticion.GET.get('id')
        nota = Nota.objects.filter(Q(pk=id) & Q(usuario=peticion.user))
        nota = nota.first()
        return render(peticion, 'notas/hacer-nota.html',{
            'nota':nota
            })
    raise PermissionDenied

def crear_nota(peticion):
    if peticion.method == 'GET' and peticion.user.is_authenticated:
        return render(peticion, 'notas/hacer-nota.html',{
            'nota':None
        })
    raise PermissionDenied