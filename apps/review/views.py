from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Review
from .serializers import ReviewSerializer


# Create your views here.
class ReviewViewSet(viewsets.ModelViewSet):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'user_id']
