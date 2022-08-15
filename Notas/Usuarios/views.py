#Controlador
from django.shortcuts import render, redirect

# Nos ayuda a crear formularios automáticamente
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrarUsuarioForm, IniciarSesionForm

# Permite responder la peticion
from django.contrib import messages
# Permite usar el login y la autenticación que trae django
from django.contrib.auth import login, authenticate

def registrarse(peticion):
    if peticion.method == 'POST':
        #form = UserCreationForm(peticion.POST)
        form = RegistrarUsuarioForm(peticion.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(peticion, 'Cuenta creada.')
            password = form.cleaned_data.get('password1')
            usuario = authenticate(peticion, email=usuario.email, password=password)
            login(peticion, usuario)
            return redirect('mis-notas')
    else:
        #form = UserCreationForm()
        form = RegistrarUsuarioForm()
    return render(peticion, 'usuarios/registrarse.html', {'form': form})



