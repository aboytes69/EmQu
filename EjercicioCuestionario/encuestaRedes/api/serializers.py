from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError, transaction
from encuestaRedes.models import RedesSociales, Participantes, DatosRedes


class SerializerPollIn(serializers.Serializer):
    correo = serializers.EmailField(allow_null=False, allow_blank=False)
    edad = serializers.CharField(allow_null=False)
    sexo = serializers.CharField(allow_blank=True, default='N')
    favorita = serializers.IntegerField(allow_null=True)
    datos_redes = serializers.ListField(allow_null=False, allow_empty=False)

    def validate_correo(self, value: str) -> str:
        if Participantes.objects.filter(correo=value).exists():
            raise ValidationError("Correo ya registrado")
        return value

    def validate_edad(self, value: str) -> str:
        value.upper()
        validate = None
        for dato in Participantes.rangos_edad:
            if value in dato:
                validate = dato
        if validate is None:
            raise ValidationError("opcion no disponible " + str(value))
        return value

    def validate_sexo(self, value: str) -> str:
        value.upper()
        if not value:
            value = "N"
        validate = None
        for dato in Participantes.sexo_choices:
            if value in dato:
                validate = dato
        if validate is None:
            raise ValidationError("opcion no disponible " + str(value))
        return value

    def validate_datos_redes(self, value: list) -> list:
        lista_error = []
        for dato in value:
            red = dato.get('red_social')
            existe_red = RedesSociales.objects.filter(nombre_red_social__contains=red).exists()
            if not existe_red:
                lista_error.append("No existe " + str(dato.get('red_social')))
        if lista_error:
            raise ValidationError({'status': lista_error})
        return value

    def create(self, validated_data):
        """Creamos el registro en la tabla participantes
        y se añaden los registros en la tabla DatosRedes"""
        lista_redes = validated_data.get('datos_redes')
        validated_data.pop('datos_redes')
        try:
            with transaction.atomic():
                registro_instance = Participantes.objects.create(
                    correo=validated_data.get('correo'),
                    edad=validated_data.get('edad'),
                    sexo=validated_data.get('sexo'),
                    favorita_id=validated_data.get('favorita')
                )

                for dato in lista_redes:
                    red = RedesSociales.objects.get(nombre_red_social=dato.get('red_social'))
                    DatosRedes.objects.create(
                        usuario_relacionado=registro_instance,
                        red_social=red,
                        horas=dato.get('horas')
                    )
        except IntegrityError:
            raise ValueError("Error de base de datos")
        return True
