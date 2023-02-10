from django.urls import path, include

from apps.review.views import ReviewViewSet

urlpatterns = [
	path('', ReviewViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
]
