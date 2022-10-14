# Generated by Django 4.1.1 on 2022-09-23 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoC', models.CharField(help_text='Ingrese el Codigo del Cliente', max_length=100)),
                ('nombreCliente', models.CharField(help_text='Ingrese el Nombre del Cliente', max_length=100)),
                ('apellidoCliente', models.CharField(help_text='Ingrese el Apellido del Cliente', max_length=100)),
                ('direccionCliente', models.CharField(help_text='Ingrese la Direccion del Cliente', max_length=100)),
                ('telefonoCliente', models.CharField(help_text='Ingrese el Telefono del Cliente', max_length=12)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Comprar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechadecompra', models.CharField(max_length=100, verbose_name='fecha de compra')),
                ('codigoC', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('codigoproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
            options={
                'verbose_name': 'Cantidad de distribucion',
                'verbose_name_plural': 'Cantidad de distribuciones',
            },
        ),
    ]
