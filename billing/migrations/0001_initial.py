# Generated by Django 3.2.9 on 2021-12-04 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.PositiveSmallIntegerField(choices=[(0, 'Agua'), (1, 'Luz'), (2, 'Telefono'), (3, 'Internet'), (4, 'Gas')], verbose_name='Servicio')),
                ('description', models.CharField(max_length=100, verbose_name='Descripción')),
                ('deadline', models.DateField(verbose_name='Fecha de vencimiento')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Importe')),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Pending'), (1, 'Paid'), (2, 'Cancelled')], verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Boleta de pago',
                'verbose_name_plural': 'Boletas de pago',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Importe')),
                ('card_number', models.CharField(max_length=16, null=True, verbose_name='Número de tarjeta')),
                ('date', models.DateField(verbose_name='Fecha de pago')),
                ('payable', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='billing.payable', verbose_name='Factura')),
            ],
            options={
                'verbose_name': 'Transacción',
                'verbose_name_plural': 'Transacciones',
            },
        ),
    ]
