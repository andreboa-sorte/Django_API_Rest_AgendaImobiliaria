# Generated by Django 3.2.7 on 2021-09-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendaImoveis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaimoveis',
            name='codigoReserva',
            field=models.CharField(default='', max_length=10),
        ),
    ]
