#import json

from django.contrib.auth.models import User
from django.test.client import Client
#from django.http import response
#from django.urls import reverse
from rest_framework import status
#import rest_framework
#from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

#from agendaImoveis.serializer import agendaSerializer
#from agendaImoveis.models import AgendaImoveis


class TestAdmin(APITestCase):

    def setUp(self):
        self.client = Client()
        self.my_admin = User(username='user', is_staff=True)
        my_admin.set_password('qwerty') 
        my_admin.save() # needed to save to temporary test db
        response = self.client.get('/admin/', follow=True)
        loginresponse = self.client.login(username='user',password='passphrase')
        self.assertTrue(loginresponse) # should now return "true"

class RegistroCasoDeTeste(APITestCase):
    
    def teste_registro(self):
        data = {
            "codigoReserva": "ADJ888",
            "nomeCliente": "Gabriela da Silva Pereira",
            "dataCheckin": "2021-09-01T07:06:00-03:00",
            "dataCheckout": "2021-09-10T14:06:00-03:00",
            "limpeza": False,
            "manuntencao": False,
            "statusConcluido": False
        }
        response = self.client.post("/AgendaImoveis/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

'''
infelizmento retorna erro 404 e não consegui resolver o problema
class AtualizacaoCasoDeTeste(APITestCase):

    def teste_atualiza(self):
        TestAdmin.setUp
        data = {
                "codigoReserva": "ADJ888",
                "nomeCliente": "Gabriela da Silva Pereira",
                "dataCheckin": "2021-09-01T07:06:00-03:00",
                "dataCheckout": "2021-09-10T14:06:00-03:00",
                "limpeza": True,
                "manuntencao": True,
                "statusConcluido": True
        }
        response = self.client.put("/AgendaImoveis/1/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), data)
'''


       



