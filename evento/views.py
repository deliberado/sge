from django.shortcuts import render
from evento.models import Evento


def home_eventos(request):
    lista_eventos = Evento.objects.all()
    return render(request, 'index.html', context={'eventos':lista_eventos})


def home_evento(request, evento_id):
    return render(request, 'evento.html', context=None)