from .models import Producto, Cliente,  Factura, DetalleFactura
from django.contrib import admin

class ProductoAdmin(admin.ModelAdmin):
    # readonly_fields = ['creacion', 'modificacion']
    list_display = ('descripcion', 'precio', 'stock', 'iva')
    ordering = ('descripcion',)
    search_fields = ('descripcion','stock')
    list_filter = ('descripcion',)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(DetalleFactura)


