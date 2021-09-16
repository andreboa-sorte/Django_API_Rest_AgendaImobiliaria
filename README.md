# Django_API_Rest_AgendaImobiliaria

### Aplicação Django com API Rest Framework de uma Agencia Imobiliária.

<div align="center">
  
  ### Vídeo mostrando o codigo
  [![IMAGE ALT TEXT HERE](https://soshace.com/wp-content/uploads/2021/01/879-png-3.png)](https://youtu.be/bBalsMWKDlY) 
  <br>
  ### *(Clique na imamge para ser redirecionado)*
 
</div>

***

**Qual o objetivo?**
* Criar uma BackEnd que retorne para um agenda os seguntes Dados:<br> 
> Id da reserva. <br>
> Nome do cliente. <br>
> CheckIn. <br>
> CheckOut. <br>
> Status da limpeza. <br>
> Status da manutenção. <br>
> Status do encerramento / conclusão do pedido. <br>


**Itens ultilizados e versoniamentos:**
* Python 3.9.0
* asgiref 3.4.1
* Django 3.2.7
* djangorestframework 3.12.4
* pytz 2021.1
* sqlparse 0.4.2

***

**Qual é o usuario e senha do Admin?** <br>
User = user <br>
Email = ' ' <br>
Senha = qwerty <br>

**Posue teste automatizado?**
> No arquivo *tests.py* somente posue o teste de **POST**, pois infelizmente os ourtos metodos(PUT, GET e DELETE) retornaram erro 404 e mesmo pesqusiando intensamente, não consegui achar como concertar o erro. Então somente posue o metodo POST. <br>
> Durante o video demonstrativo do codigo, é demonstrado de maneira manual o teste dos metodos **GET, POST, PUT e DELETE**.

**Preciso baixar algo?**<br>
Somente é necessario ter o Python instalado e uma IDE de sua preferencia.<br>
Não ha necessidade de baixar o Django e nenhuma extenção a mais;<br>
Dentro do codigo, posue a <strong>venv</strong> com os intens instalados.

<strong>Como faço para funcionar o codigo?</strong>
* Basta baixar ou clonar o codigo, depois abrir em uma IDE e dentro do terminal dar o comando **python manage.py startserver**.<br> 
* Depois basta entrar na porta do Local Host e assesar a API.




