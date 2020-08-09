from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductoForm
from .models import Producto, Cliente

def producto(request):
    opciones = {'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarproducto')
    else:
        form = ProductoForm()
        opciones['form'] = form
    return render(request, './Producto/create.html', opciones)

def listarProducto(request):
    producto = Producto.objects.all()
    query = {'productos': producto}
    return render(request, './Producto/consultar.html', query)

def editarProducto(request, id):
    opciones = {'accion': 'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/listarproducto')
    return render(request, './Producto/create.html', opciones)
def Menu(request):
    return render(request, 'principal.html')

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        # return redirect('/listarproducto')
    return render(request, './Producto/delete.html', {'Producto':producto})

