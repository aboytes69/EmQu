# Generated by Django 3.1.2 on 2022-08-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestaRedes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantes',
            name='edad',
            field=models.CharField(choices=[('A', '18-25'), ('B', '26-33'), ('C', '34-40'), ('D', '41+')], max_length=1),
        ),
        migrations.AlterField(
            model_name='participantes',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N', 'No responde')], max_length=1),
        ),
    ]
