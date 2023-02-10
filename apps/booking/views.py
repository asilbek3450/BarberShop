from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Booking, Promocode
from .serializers import BookingSerializer, PromocodeSerializer


class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'barber_id', 'user_id']
	
	
class PromocodeViewSet(viewsets.ModelViewSet):
	queryset = Promocode.objects.all()
	serializer_class = PromocodeSerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'discount']
	