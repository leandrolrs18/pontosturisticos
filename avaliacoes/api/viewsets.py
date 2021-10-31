from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer