from celery import Celery
from random import choice

from sistema_gestao_propostas.celery import app
from api.models import Proposta


app = Celery("tasks", broker="pyamqp://guest:guest@rabbitmq:5672//")

@app.task
def avaliar_proposta(proposta_id):
    proposta = Proposta.objects.get(id=proposta_id)
    proposta.situacao = 'Negada'

    # Para fins de teste, desenvolva um algoritmo onde metade das propostas serão negadas e metade serão aprovadas.
    resultado = choice([True, False])
    
    if resultado:
        proposta.situacao = 'Aprovada'
    else:
        proposta.situacao = 'Negada'

    proposta.save()
