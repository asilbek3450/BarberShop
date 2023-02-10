from django.urls import path, include

urlpatterns = [
    path('barbers/', include('barbers.urls')),
    path('booking/', include('booking.urls')),
    path('review/', include('review.urls')),
    path('service/', include('service.urls')),
    path('shops/', include('shops.urls')),
    path('users/', include('users.urls')),
]
