from django.db import models


class Tipo(models.Model):
    nome = models.CharField('Nome', max_length=150)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField('Nome o evento', max_length=150)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome
