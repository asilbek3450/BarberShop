from django.urls import path, include

from apps.booking.views import BookingViewSet, PromocodeViewSet

urlpatterns = [
	path('', BookingViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
	path('promocodes/', PromocodeViewSet.as_view({'get': 'list', 'post': 'create'})),
]
