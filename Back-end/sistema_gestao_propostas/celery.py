import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_gestao_propostas.settings')

broker_url = 'amqp://guest@rabbitmq:5672//'

app = Celery('sistema_gestao_propostas')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
