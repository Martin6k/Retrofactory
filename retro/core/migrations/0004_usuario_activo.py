# Generated by Django 5.0.6 on 2024-07-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_usuario_rut_alter_usuario_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='activo',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]