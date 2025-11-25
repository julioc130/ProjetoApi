from django.db import models

class Nota(models.Model):
    aluno_id = models.IntegerField()   # id vindo do serviço 1
    curso_id = models.IntegerField()   # idem
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
