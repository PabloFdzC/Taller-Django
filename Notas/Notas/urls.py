"""Notas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from Usuarios import views as VistaUsuarios
from ManejoNotas import views as VistaManejoNotas

urlpatterns = [
    # Aquí se pueden ver las tablas de las bases de datos
    path('admin/', admin.site.urls),
    
    # Muestra el formulario para registrarse o si es post registra un usuario
    path('registrarse/', VistaUsuarios.registrarse, name='registrarse'),
    # Muestra el formulario para iniciar sesión o si es post inicia sesión
    path('iniciar-sesion/', auth_views.LoginView.as_view(
        template_name='usuarios/iniciar-sesion.html',
        next_page='/mis-notas/'), name='iniciar-sesion'),
    # Cierra sesión y lo devuelve a la ventana de iniciar sesión
    path('cerrar-sesion/', auth_views.LogoutView.as_view(next_page='/iniciar-sesion/'), name='cerrar-sesion'),
    # Si se está autenticado muestra la ventana de mis notas, sino lo manda
    # a iniciar sesión
    path('mis-notas/', VistaManejoNotas.mis_notas, name='mis-notas'),
    # Muestra una lista con las notas del usuario
    path('ver-mis-notas/', VistaManejoNotas.ver_mis_notas, name='ver-mis-notas'),
    # Guarda la nota ya sea que la esté editando o creando, si la está editando
    # se debe enviar el id de la nota
    path('guardar-nota/', VistaManejoNotas.guardar_nota, name='guardar-nota'),
    # Borra una nota según el id
    path('borrar-nota/', VistaManejoNotas.borrar_nota, name='borrar-nota'),
]
