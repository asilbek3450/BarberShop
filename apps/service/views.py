from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Service
from .serializers import ServiceSerializer


# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'title', 'price']
