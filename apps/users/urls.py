from django.urls import path

from apps.users.views import UserViewSet

urlpatterns = [
	path('', UserViewSet.as_view({'get': 'list'}), name='user-list'),
]
