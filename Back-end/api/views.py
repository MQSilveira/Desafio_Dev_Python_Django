from rest_framework import viewsets

from . serializers import PropostaSerializer
from . models import Proposta

from .tasks import avaliar_proposta
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["POST"])
def nova_proposta(request):
    serializer = PropostaSerializer(data=request.data)
    if serializer.is_valid():
        proposta = serializer.save()
        avaliar_proposta.delay(proposta.id)
        return Response({'message': 'Nova proposta criada com sucesso!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_propostas(request):
    queryset = Proposta.objects.all()
    serializer = PropostaSerializer(queryset, many=True)
    return Response(serializer.data)

