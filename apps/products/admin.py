from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'color', 'size', 'price', 'stock', 'deleted')
    list_filter = ('brand', 'color', 'size', 'deleted')  # Filtros en la barra lateral
    search_fields = ('name', 'brand__name')  # Campos de búsqueda
    list_editable = ('price', 'stock')  # Campos editables directamente desde la lista

admin.site.register(Product, ProductAdmin)
