from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Usuario

# Esta clase nos ayuda a indicar qué se muestra en la
# pantalla del admin
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'is_staff', 'last_login', 'password')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(Usuario, UserAdmin)