from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
	search_fields = ['username']
	
	