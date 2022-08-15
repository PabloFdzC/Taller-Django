from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

# Nos ayuda a crear usuarios con las herramientas que tiene Django
class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, primary_key=True, unique=True)

    # Los siguientes campos son necesarios porque estamos usando la clase
    # AbstractBaseUser
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Este es necesario por la biblioteca que estamos usando para
    # crear automaticamente el formulario. Lo ocupa porque por
    # defecto se necesita un campo para identificar a los usuarios
    # en este caso se usa el username, pero uno lo puede cambiar,
    # como lo hacemos aquí
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    # Se recomienda quitar al email de los campos requeridos porque
    # lo estamos poniendo como identificador
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
