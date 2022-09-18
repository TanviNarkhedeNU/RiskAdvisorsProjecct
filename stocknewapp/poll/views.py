from django.shortcuts import render
from poll.serializer import EquitiesSerializer
from poll.serializer import ReturnsSerializer
from rest_framework import viewsets
from .models import Equities, Returns


class EquitiesView(viewsets.ModelViewSet):
    serializer_class = EquitiesSerializer
    queryset = Equities.objects.all()


class ReturnsView(viewsets.ModelViewSet):
    serializer_class = ReturnsSerializer
    queryset = Returns.objects.all()
