from django.contrib import admin

from .models import Staff, StaffRole

class StaffAdmin(admin.ModelAdmin):
    list_display = ('names', 'lastnames', 'email', 'role', 'document_number', 'deleted')
    list_filter = ('role', 'deleted')  # Filtros en la barra lateral
    search_fields = ('names', 'lastnames', 'email', 'document_number')  # Campos de búsqueda

admin.site.register(Staff, StaffAdmin)

class StaffRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'permissions', 'deleted')
    search_fields = ('name',)

admin.site.register(StaffRole, StaffRoleAdmin)
