from django.db.models import fields
from rest_framework import serializers
from agendaImoveis.models import AgendaImoveis

class agendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaImoveis
        fields = ['codigoReserva', 'nomeCliente', 'dataCheckin', 'dataCheckout',
                    'limpeza', 'manuntencao', 'statusConcluido']
        