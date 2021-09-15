from django.contrib import admin
from agendaImoveis.models import AgendaImoveis

# Register your models here.

class agenda(admin.ModelAdmin):
    list_display = ('codigoReserva', 'nomeCliente', 'dataCheckin', 'dataCheckout',
                     'limpeza', 'manuntencao', 'statusConcluido')
    list_display_links = ('limpeza', 'manuntencao', 'statusConcluido')
    search_fields = ('codigoReserva', 'nomeCliente')


admin.site.register(AgendaImoveis, agenda)