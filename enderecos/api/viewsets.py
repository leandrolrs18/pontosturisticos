from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer