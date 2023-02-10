from django.contrib import admin

from .models import Barber, BarberImage

# Register your models here.
admin.site.register(Barber)
admin.site.register(BarberImage)
