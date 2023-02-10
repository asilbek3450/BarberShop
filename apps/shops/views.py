from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Shop
from .serializers import ShopSerializer


class ShopViewSet(viewsets.ModelViewSet):
	queryset = Shop.objects.all()
	serializer_class = ShopSerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'title', 'price']
	