from django.contrib import admin

from .models import Nota

# Esta clase nos ayuda a indicar qué se muestra en la
# pantalla del admin
class NotaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'texto',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

admin.site.register(Nota, NotaAdmin)
