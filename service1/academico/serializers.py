from rest_framework import serializers
from .models import Aluno, Curso, Matricula

class AlunoInDTO(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    idade = serializers.IntegerField(min_value=0)

    def validate_nome(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Nome deve ter pelo menos 3 caracteres.")
        return value


class AlunoOutDTO(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["id", "nome", "email", "idade"]


class CursoDTO(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ["id", "nome", "carga_horaria"]


class MatriculaInDTO(serializers.Serializer):
    aluno_id = serializers.IntegerField()
    curso_id = serializers.IntegerField()

    def validate(self, attrs):
        # exemplo: você pode colocar regras de negócio aqui
        return attrs


class MatriculaOutDTO(serializers.ModelSerializer):
    aluno = AlunoOutDTO()
    curso = CursoDTO()

    class Meta:
        model = Matricula
        fields = ["id", "aluno", "curso", "data_matricula"]
