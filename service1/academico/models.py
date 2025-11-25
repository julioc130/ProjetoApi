from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="matriculas")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="matriculas")
    data_matricula = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("aluno", "curso")  # impede dupla matrícula no mesmo curso
