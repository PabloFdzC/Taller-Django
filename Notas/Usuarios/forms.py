#Controlador
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Estas clases nos ayudan a crear los formularios automáticamente
class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'password1', 'password2']

class IniciarSesionForm(AuthenticationForm):
    
    class Meta:
        model = Usuario
        fields = ['email', 'password']