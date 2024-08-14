from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'cedula', 'telefono', 'celular1', 'celular2', 'direccion',
                  'sillas', 'mesa_4', 'meson_10', 'forros_silla', 'cintas_silla',
                  'manteles_grandes', 'manteles_pequeños', 'sillas_niño', 'copa_champaña']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'celular1': forms.TextInput(attrs={'class': 'form-control'}),
            'celular2': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'sillas': forms.NumberInput(attrs={'class': 'form-control'}),
            'mesa_4': forms.NumberInput(attrs={'class': 'form-control'}),
            'meson_10': forms.NumberInput(attrs={'class': 'form-control'}),
            'forros_silla': forms.NumberInput(attrs={'class': 'form-control'}),
            'cintas_silla': forms.NumberInput(attrs={'class': 'form-control'}),
            'manteles_grandes': forms.NumberInput(attrs={'class': 'form-control'}),
            'manteles_pequeños': forms.NumberInput(attrs={'class': 'form-control'}),
            'sillas_niño': forms.NumberInput(attrs={'class': 'form-control'}),
            'copa_champaña': forms.NumberInput(attrs={'class': 'form-control'}),
        }
