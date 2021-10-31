from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from rest_framework.fields import SerializerMethodField

class PontoTuristicoSerializer(ModelSerializer):
    
    atracoes = AtracaoSerializer(many=True) # tem atracoes como todo
    descricao_completa = SerializerMethodField()
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'descricao_completa', 'descricao_completa2']

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)