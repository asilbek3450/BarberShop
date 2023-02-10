from django.urls import path, include

from apps.barbers.views import BarberImageViewSet, BarberViewSet

urlpatterns = [
	path('', BarberViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
	path('images/', BarberImageViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
]
