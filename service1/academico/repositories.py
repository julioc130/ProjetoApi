from typing import Optional
from .models import Aluno, Curso, Matricula

class AlunoRepository:
    @staticmethod
    def listar():
        return Aluno.objects.all()

    @staticmethod
    def buscar_por_id(aluno_id: int) -> Optional[Aluno]:
        return Aluno.objects.filter(id=aluno_id).first()

    @staticmethod
    def criar(**dados):
        return Aluno.objects.create(**dados)

    @staticmethod
    def atualizar(aluno: Aluno, **dados):
        for campo, valor in dados.items():
            setattr(aluno, campo, valor)
        aluno.save()
        return aluno

    @staticmethod
    def deletar(aluno: Aluno):
        aluno.delete()


class CursoRepository:
    @staticmethod
    def listar():
        return Curso.objects.all()

    @staticmethod
    def criar(**dados):
        return Curso.objects.create(**dados)


class MatriculaRepository:
    @staticmethod
    def criar(aluno: Aluno, curso: Curso):
        return Matricula.objects.create(aluno=aluno, curso=curso)

    @staticmethod
    def listar():
        return Matricula.objects.select_related("aluno", "curso").all()
