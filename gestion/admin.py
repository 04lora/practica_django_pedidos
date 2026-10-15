from django.contrib import admin

# Register your models here.
from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]

    numero_pedido = models.CharField(max_length=50, unique=True)
    cliente = models.CharField(max_length=150)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    valor_total = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')

    def __str__(self):
        return f"Pedido #{self.numero_pedido} - {self.cliente}"