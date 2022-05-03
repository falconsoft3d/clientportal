from django.db import models
from accounts.models import Account


# Create your models here.
class Ticket(models.Model):
    STATUS = (
        ('New', 'Nuevo'),
        ('Sent', 'Enviado'),
        ('Sale', 'Pedido de Venta'),
        ('dispatched', 'Despachado'),
        ('Invoiced', 'Facturado'),
        ('Cancel', 'Cancelado'),
    )
    name = models.CharField(blank=True, max_length=200)
    text = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default='New')

    def __str__(self):
        return self.name
