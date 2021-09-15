# Generated by Django 3.2.7 on 2021-09-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaImoveis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoReserva', models.CharField(default='', editable=False, max_length=10)),
                ('nomeCliente', models.CharField(max_length=30)),
                ('dataCheckin', models.DateTimeField()),
                ('dataCheckout', models.DateTimeField()),
                ('limpeza', models.BooleanField(default=False)),
                ('manuntencao', models.BooleanField(blank=True, default=False)),
                ('statusConcluido', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]