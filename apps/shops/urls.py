from django.urls import path, include

from apps.shops.views import ShopViewSet
from shared.rest_framework.router import OptionalSlashRouter

router = OptionalSlashRouter()

router.register('shop', ShopViewSet, 'shop')

urlpatterns = [
	path('', include(router.urls))
]
