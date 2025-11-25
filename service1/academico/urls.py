from django.urls import path
from .views import alunos_view, aluno_detalhe_view, matriculas_view

urlpatterns = [
    path("alunos/", alunos_view, name="alunos"),
    path("alunos/<int:aluno_id>/", aluno_detalhe_view, name="aluno-detalhe"),
    path("matriculas/", matriculas_view, name="matriculas"),
]
