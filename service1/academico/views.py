from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    AlunoInDTO,
    AlunoOutDTO,
    MatriculaInDTO,
    MatriculaOutDTO,
)
from .repositories import AlunoRepository, CursoRepository, MatriculaRepository


@api_view(["GET", "POST"])
def alunos_view(request):
    if request.method == "GET":
        alunos = AlunoRepository.listar()
        serializer = AlunoOutDTO(alunos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        dto = AlunoInDTO(data=request.data)
        if not dto.is_valid():
            return Response(dto.errors, status=status.HTTP_400_BAD_REQUEST)

        aluno = AlunoRepository.criar(**dto.validated_data)
        out = AlunoOutDTO(aluno)
        return Response(out.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def aluno_detalhe_view(request, aluno_id: int):
    aluno = AlunoRepository.buscar_por_id(aluno_id)
    if not aluno:
        return Response({"detail": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        out = AlunoOutDTO(aluno)
        return Response(out.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        dto = AlunoInDTO(data=request.data)
        if not dto.is_valid():
            return Response(dto.errors, status=status.HTTP_400_BAD_REQUEST)

        aluno_atualizado = AlunoRepository.atualizar(aluno, **dto.validated_data)
        out = AlunoOutDTO(aluno_atualizado)
        return Response(out.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        AlunoRepository.deletar(aluno)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST", "GET"])
def matriculas_view(request):
    if request.method == "POST":
        dto = MatriculaInDTO(data=request.data)
        if not dto.is_valid():
            return Response(dto.errors, status=status.HTTP_400_BAD_REQUEST)

        aluno_id = dto.validated_data["aluno_id"]
        curso_id = dto.validated_data["curso_id"]

        aluno = AlunoRepository.buscar_por_id(aluno_id)
        if not aluno:
            return Response({"detail": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        curso = CursoRepository.listar().filter(id=curso_id).first()
        if not curso:
            return Response({"detail": "Curso não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        matricula = MatriculaRepository.criar(aluno=aluno, curso=curso)
        out = MatriculaOutDTO(matricula)
        return Response(out.data, status=status.HTTP_201_CREATED)

    if request.method == "GET":
        matriculas = MatriculaRepository.listar()
        out = MatriculaOutDTO(matriculas, many=True)
        return Response(out.data, status=status.HTTP_200_OK)
