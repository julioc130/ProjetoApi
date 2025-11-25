from .models import Aluno, Curso, Matricula

class AlunoRepository:
    @staticmethod
    def listar():
        return Aluno.objects.all()

    @staticmethod
    def buscar_por_id(aluno_id: int):
        return Aluno.objects.filter(id=aluno_id).first()

    @staticmethod
    def salvar(aluno: Aluno):
        aluno.save()
        return aluno


class CursoRepository:
    @staticmethod
    def listar():
        return Curso.objects.all()


class MatriculaRepository:
    @staticmethod
    def criar(**kwargs):
        return Matricula.objects.create(**kwargs)
