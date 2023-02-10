from django.urls import path, include

from apps.shops.views import ShopViewSet

urlpatterns = [
	path('', ShopViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
]
