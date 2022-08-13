from rest_framework import routers
from django.urls import path
from encuestaRedes.api.views import *

routers = routers.SimpleRouter()
routers.register(r'RegisterPoll', RegisterPoll, basename='Registro_de_cuestionarios')

urlpatterns = [
                  # path('listUser/', ListUsers.as_view())
              ] + routers.urls