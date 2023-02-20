from django.urls import path, include

from apps.service.views import ServiceViewSet
from shared.rest_framework.router import OptionalSlashRouter

router = OptionalSlashRouter()

router.register('service', ServiceViewSet, 'service')

urlpatterns = [
	path('', include(router.urls))
	
]