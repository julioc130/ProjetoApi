from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

# LISTAR TODOS
@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# BUSCAR / ATUALIZAR POR NICK
@api_view(["GET", "PUT"])
def get_by_nick(request, nick):
    try:
        user = User.objects.get(pk=nick)
    except User.DoesNotExist:
        return Response({"detail": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Se quiser exigir JWT, descomente a permissão acima e verifique request.user
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CRUD "manager"
@api_view(["GET", "POST", "PUT", "DELETE"])
def user_manager(request):
    # GET ?user=<nick>
    if request.method == "GET":
        nick = request.GET.get("user")
        if not nick:
            return Response({"detail": "Parâmetro 'user' é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=nick)
        except User.DoesNotExist:
            return Response({"detail": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST criar
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT atualizar
    if request.method == "PUT":
        nick = request.data.get("user_nickname")
        if not nick:
            return Response({"detail": "Campo 'user_nickname' é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=nick)
        except User.DoesNotExist:
            return Response({"detail": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE deletar
    if request.method == "DELETE":
        nick = request.data.get("user_nickname")
        if not nick:
            return Response({"detail": "Campo 'user_nickname' é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=nick)
        except User.DoesNotExist:
            return Response({"detail": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
