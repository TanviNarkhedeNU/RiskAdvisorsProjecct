from django.shortcuts import render
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from poll.serializer import EquitiesSerializer
from poll.serializer import ReturnsSerializer
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from .models import Equities, Returns


class EquitiesView(viewsets.ModelViewSet):
    serializer_class = EquitiesSerializer
    queryset = Equities.objects.all()


class ReturnsView(viewsets.ModelViewSet):
    serializer_class = ReturnsSerializer
    queryset = Returns.objects.all()
