from django.urls import path, include

from apps.barbers.views import BarberImageViewSet, BarberViewSet
from shared.rest_framework.router import OptionalSlashRouter

router = OptionalSlashRouter()

router.register('barber', BarberViewSet, 'barber')
router.register('images', BarberImageViewSet, 'barber-image')

urlpatterns = [
	path('', include(router.urls))
]
