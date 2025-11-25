from rest_framework import serializers
from .models import Aluno, Curso, Matricula

class AlunoDTO(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["id", "nome", "email"]

    # Validação de campo
    def validate_nome(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Nome deve ter pelo menos 3 caracteres.")
        return value


class CursoDTO(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ["id", "nome", "carga_horaria"]


class MatriculaDTO(serializers.ModelSerializer):
    aluno_id = serializers.PrimaryKeyRelatedField(
        queryset=Aluno.objects.all(), source="aluno"
    )
    curso_id = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all(), source="curso"
    )

    class Meta:
        model = Matricula
        fields = ["id", "aluno_id", "curso_id", "data_matricula"]
        read_only_fields = ["data_matricula"]

    def validate(self, attrs):
        # aqui você pode validar regras de negócio da matrícula
        return attrs
