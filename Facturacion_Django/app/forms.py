from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion','precio','stock','iva')
        label = {'descripcion': 'Producto', 'precio': 'Precio', 'stock': 'Stock', 'iva': 'Iva'}
