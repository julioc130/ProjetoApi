from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

from . import funcoes as fn


@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        users = User.objects.all()                          #obter todos os objetos no banco de dados do usuario (retorna um conjunto de consultas)

        serializer = UserSerializer(users, many=True)       #serializar os dados do objeto em json (Tem um parametro 'many' porque e um queryset)

        return Response(serializer.data)                    #retornar os dados serializados
    
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT'])
def get_by_nick(request, nick):

    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


# CRUDZAO DA MASSA
@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['user']:                         #verifique se ha um parametro get chamado 'user' (/?user=xxxx&...)
                user_nickname = request.GET['user']         #encontrar parâmetro get
                try:
                    user = User.objects.get(pk=user_nickname)   #obter o objeto no banco de dados
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializer(user)           #rerializar os dados do objeto em json
                return Response(serializer.data)            #retornar os dados serializados

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
   

# CRIANDO DADOS

    if request.method == 'POST':

        new_user = request.data
        
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)


# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        nickname = request.data['user_nickname']

        try:
            updated_user = User.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
        print('Resultado final ', fn.soma(1,2))

        serializer = UserSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


