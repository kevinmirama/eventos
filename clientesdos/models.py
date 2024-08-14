from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    celular1 = models.CharField(max_length=15)
    celular2 = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    # Campos de cantidad para cada tipo de alquiler
    sillas = models.PositiveIntegerField(default=0)
    mesa_4 = models.PositiveIntegerField(default=0)
    meson_10 = models.PositiveIntegerField(default=0)
    forros_silla = models.PositiveIntegerField(default=0)
    cintas_silla = models.PositiveIntegerField(default=0)
    manteles_grandes = models.PositiveIntegerField(default=0)
    manteles_pequeños = models.PositiveIntegerField(default=0)
    sillas_niño = models.PositiveIntegerField(default=0)
    copa_champaña = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre
