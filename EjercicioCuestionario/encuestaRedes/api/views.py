from rest_framework import viewsets, status
from encuestaRedes.api.serializers import SerializerPollIn
from rest_framework.response import Response


class RegisterPoll(viewsets.GenericViewSet):
    """Registro de encuentas"""
    permission_classes = ()
    serializer_class = SerializerPollIn

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(data={"registro correcto"}, status=status.HTTP_201_CREATED)
