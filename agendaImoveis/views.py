from rest_framework import viewsets
from agendaImoveis import serializer
from agendaImoveis.models import AgendaImoveis
from agendaImoveis.serializer import agendaSerializer
# Create your views here.

class agendaViewSet(viewsets.ModelViewSet):
    queryset = AgendaImoveis.objects.all()
    serializer_class = agendaSerializer
