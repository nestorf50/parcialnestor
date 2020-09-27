# Generated by Django 3.1.1 on 2020-09-27 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('telefono', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agropecuaria.cliente')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agropecuaria.producto')),
            ],
        ),
    ]
