from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .serializers import BarberImageSerializer, BarberSerializer
from .models import Barber, BarberImage


class BarberViewSet(viewsets.ModelViewSet):
	queryset = Barber.objects.all()
	serializer_class = BarberSerializer
	filter_backends = [SearchFilter]
	search_fields = ['id', 'name', 'image']


class BarberImageViewSet(viewsets.ModelViewSet):
	queryset = BarberImage.objects.all()
	serializer_class = BarberImageSerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'barber_id', 'image']
	