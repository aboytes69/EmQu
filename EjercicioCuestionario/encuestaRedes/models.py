from django.db import models


class RedesSociales(models.Model):
    """Redes sociales"""
    id = models.AutoField(primary_key=True, editable=False)
    nombre_red_social = models.CharField(max_length=20, null=False)


class Participantes(models.Model):
    """Tabla para registro de participantes de la encuesta"""
    rangos_edad = (('A', '18-25'), ('B', '26-33'), ('C', '34-40'), ('D', '41+'))
    sexo_choices = (('M', 'Masculino'), ('F', 'Femenino'), ('N', 'No responde'))
    correo = models.EmailField(primary_key=True, editable=False, null=False, blank=False)
    edad = models.CharField(max_length=1, choices=rangos_edad, null=False, blank=False)
    sexo = models.CharField(choices=sexo_choices, null=False, blank=False, max_length=1)
    favorita = models.ForeignKey(RedesSociales, on_delete=models.SET_NULL, null=True)


class DatosRedes(models.Model):
    """Tabla de relacion entre participantes y redes"""
    id = models.AutoField(primary_key=True, editable=False)
    red_social = models.ForeignKey(RedesSociales, on_delete=models.CASCADE)
    horas = models.FloatField(null=False, blank=False, default=0)
    usuario_relacionado = models.ForeignKey(Participantes, on_delete=models.SET_NULL, null=True)
