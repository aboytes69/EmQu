# Generated by Django 3.1.2 on 2022-08-13 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestaRedes', '0002_auto_20220812_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosredes',
            name='usuario_relacionado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='encuestaRedes.participantes'),
        ),
    ]
