from django.urls import path, include

from apps.booking.views import BookingViewSet, PromocodeViewSet
from shared.rest_framework.router import OptionalSlashRouter

router = OptionalSlashRouter()

router.register('booking', BookingViewSet, 'booking')
router.register('promocode', PromocodeViewSet, 'promocode')

urlpatterns = [
	path('', include(router.urls))
]
