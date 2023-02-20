from django.urls import path, include

from apps.review.views import ReviewViewSet
from shared.rest_framework.router import OptionalSlashRouter

router = OptionalSlashRouter()

router.register('review', ReviewViewSet, 'review')

urlpatterns = [
	path('', include(router.urls))
]

