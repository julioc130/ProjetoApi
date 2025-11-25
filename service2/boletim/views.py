from rest_framework import viewsets, permissions
from .models import Nota
from .serializers import NotaDTO


class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaDTO
    permission_classes = [permissions.IsAuthenticated]
