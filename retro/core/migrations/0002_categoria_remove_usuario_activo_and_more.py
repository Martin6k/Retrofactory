# Generated by Django 5.0.6 on 2024-06-26 01:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('categoria', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellido_materno',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellido_paterno',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.AddField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(default='null', max_length=15),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=80),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('id_categoria', models.ForeignKey(db_column='idCategoria', on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
