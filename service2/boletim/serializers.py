from rest_framework import serializers
from .models import Nota

class NotaDTO(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ["id", "aluno_id", "curso_id", "valor", "criado_em", "atualizado_em"]

    def validate_valor(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("A nota deve estar entre 0 e 10.")
        return value
