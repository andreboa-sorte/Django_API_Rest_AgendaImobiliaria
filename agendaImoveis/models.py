from django.db import models

# Create your models here.
class AgendaImoveis(models.Model):
    codigoReserva = models.CharField(default='', blank=False, max_length=10)
    nomeCliente = models.CharField(editable=True, blank=False, max_length=30)
    dataCheckin = models.DateTimeField(editable=True, blank=False)
    dataCheckout = models.DateTimeField(editable=True, blank=False)
    limpeza = models.BooleanField(default=False, editable=True)
    manuntencao = models.BooleanField(default=False, editable=True, blank=True)
    statusConcluido = models.BooleanField(default=False, editable=True, blank=True)

    def __str__ (self):
        return self.codigoReserva

