from django.shortcuts import render
from rest_framework import viewsets

from api.models import Table
from api.serializers import TableSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
