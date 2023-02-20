from django.urls import path, include

from apps.users.views import UserViewSet
from shared.rest_framework.router import OptionalSlashRouter

router = OptionalSlashRouter()

router.register('user', UserViewSet, 'user')

urlpatterns = [
	path('', include(router.urls))
]
