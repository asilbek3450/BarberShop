"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Barber Shop CORE API",
        default_version='v1',
        description=f"This core functionalities of all Asilbek's projects",
        contact=openapi.Contact(email="asilbekmirolimov@gmail.com")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = \
    [
        path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        path('admin/', admin.site.urls),
        path('api/v1/', include('apps.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]
