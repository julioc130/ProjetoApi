from django.urls import path
from .views import AlunoListCreateView

urlpatterns = [
    path("alunos/", AlunoListCreateView.as_view(), name="aluno-list-create"),
]