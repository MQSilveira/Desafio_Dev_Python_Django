from django.urls import path

from . views import nova_proposta, get_propostas


urlpatterns = [
    path("propostas/nova/", nova_proposta, name="nova_proposta"),
    path("propostas/", get_propostas, name="get_propostas"),
]
