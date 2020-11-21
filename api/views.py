from django.shortcuts import render

from rest_framework import viewsets

from .serializers import HerosSerializer
from .models import Heros

# Create your views here.

class HerosViewSet(viewsets.ModelViewSet):
    queryset = Heros.objects.all().order_by('name')
    serializer_class = HerosSerializer

