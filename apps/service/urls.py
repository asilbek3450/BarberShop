from django.urls import path

from apps.service.views import ServiceViewSet

urlpatterns = [
	path('', ServiceViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
]