import rest_framework
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', '=descricao', '^endereco__linha1']
    #permission_classes = [IsAuthenticated,]  #tipo de permissao
    #authentication_classes = (TokenAuthentication, ) # chave da autenticacao
    
    #lookup_field = 'nome'
    #A classe model já tem construido as funções de get, delete etc, mas elas podem ser 
    # mudadas quando como abaixo
    # 1. define qual model está sendo trabalhado, ele pode ser filtrado ou ser ele total
    def get_queryset(self):
        id = self.request.query_params.get('id', None) # id = 5, p.e
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome) # __iexact é para ser insesitivel a maisc e minus

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
    #2. a cada get pode ser requerido uma mensagem
    #def list(self, request, *args, **kwargs):
    #    return Response({'teste': 123})
    #3. quando é feito o Post:
    def create(self, request, *args, **kwargs):
        return  super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
        #return Response({'Hello': request.data['nome']})
    # 4. antes de Deletar pode ser requisitada algumas condições
    #def destroy(self, request, *args, **kwargs):
    #    pass
    # um Get num elemento
    #def retrieve(self, request, *args, **kwargs):
    #    pass
    # update/Put total de um elemento
    #def update(self, request, *args, **kwargs):
    #    pass
    # update de alguns campos
    #def partial_update(self, request, *args, **kwargs):
    #    pass
    # Algumas vezes podem ser realizadas ações, quando chamados 
    # tais urls. Quando detail for true é porque precisa ser 
    # especificado o elemento
    #@action(methods=['get', 'post'], detail=True)
    #def denunciar(self, request, pk=None):
    #    pass

    #@action(methods=['get'], detail=False)
    #def teste(self, request):
    #    pass
