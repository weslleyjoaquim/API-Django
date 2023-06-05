from rest_framework.viewsets import ModelViewSet
from .models import Grupo, Usuario
from .serializers import GrupoSerializer, UsuarioSerializer

class GrupoViewSet(ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


