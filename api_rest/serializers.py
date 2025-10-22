from rest_framework import serializers
from .models import Task, UserProfile, Group
from django.contrib.auth.models import User

# Aonde vai comecar
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# DTO de entrada (validacao de dados recebidos)
class UserInDTO(serializers.Serializer):
    user_nickname = serializers.CharField(max_length=100)
    user_name = serializers.CharField(max_length=150)
    user_email = serializers.EmailField()
    user_age = serializers.IntegerField(min_value=0)

    def validate_user_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Nome não pode ser vazio")
        return value

# DTO de saida basico
class UserOutDTO(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

# Projecao de tarefas
class TaskDTO(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "done"]

# DTO de saida detalhado (1:n embutido)
class UserDetailOutDTO(serializers.ModelSerializer):
    tasks = TaskDTO(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["user_nickname", "user_name", "user_email", "user_age", "tasks"]
