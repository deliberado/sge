from django.shortcuts import render, redirect
from evento.models import Evento, Tipo


def home_eventos(request):
    lista_eventos = Evento.objects.all()
    return render(request, 'index.html', context={'eventos':lista_eventos})


def home_evento(request, evento_id):
    return render(request, 'evento.html', context=None)


def lista_tipos(request):
    lista_tipos = Tipo.objects.all()
    return render(request, 'tipo.html', context={'tipos':lista_tipos})

def create_tipo(request):
    return render(request, 'tipo_add.html', context=None)

def salvar_tipo(request):
    nome = request.POST.get('nome_tipo')
    if nome:
        tipo = Tipo()
        tipo.nome = nome
        tipo.save()
        return redirect('/tipos')