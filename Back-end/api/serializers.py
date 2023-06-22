from rest_framework import serializers
from api.models import Proposta


class PropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta
        fields = '__all__'
