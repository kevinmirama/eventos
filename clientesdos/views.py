from django.shortcuts import render, redirect
from .forms import ClienteForm
from firebase_admin import firestore
from django.contrib import messages
from datetime import datetime

db = firestore.client()


def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            if not cliente.fecha:
                cliente.fecha = datetime.now().date()

            try:
                # Guardar el cliente en Firestore
                cliente_data = {
                    'nombre': cliente.nombre,
                    'cedula': cliente.cedula,
                    'telefono': cliente.telefono,
                    'celular1': cliente.celular1,
                    'celular2': cliente.celular2,
                    'direccion': cliente.direccion,
                    'fecha': cliente.fecha.isoformat() if cliente.fecha else None,
                    'sillas': cliente.sillas,
                    'mesa_4': cliente.mesa_4,
                    'meson_10': cliente.meson_10,
                    'forros_silla': cliente.forros_silla,
                    'cintas_silla': cliente.cintas_silla,
                    'manteles_grandes': cliente.manteles_grandes,
                    'manteles_pequeños': cliente.manteles_pequeños,
                    'sillas_niño': cliente.sillas_niño,
                    'copa_champaña': cliente.copa_champaña
                }
                db.collection('clientes').add(cliente_data)
                messages.success(request, 'Cliente registrado exitosamente.')
                return redirect('registrar_cliente')
            except Exception as e:
                messages.error(
                    request, f'Error al registrar el cliente: {str(e)}')
    else:
        form = ClienteForm()

    return render(request, 'clientes/registro_cliente.html', {'form': form})
