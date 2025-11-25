from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AlunoDTO
from .repositories import AlunoRepository


class AlunoListCreateView(APIView):
    def get(self, request):
        alunos = AlunoRepository.listar()
        serializer = AlunoDTO(alunos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AlunoDTO(data=request.data)
        if serializer.is_valid():
            aluno = serializer.save()  # mapper: DTO -> model
            return Response(AlunoDTO(aluno).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

