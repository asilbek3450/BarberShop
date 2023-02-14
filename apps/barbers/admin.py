from django.contrib import admin
from django.utils.safestring import mark_safe

import apps.barbers.serializers
from .models import Barber, BarberImage


class BarberImageAdmin(admin.ModelAdmin):
	list_display = [
		"id", "show_image"
	]
	
	def show_image(self, obj):
		if obj.image:
			return mark_safe(
				'<img src="/media/{url}" width="auto" height="50" >'.format(
					url=obj.image.url.split("/media/")[-1])
			)
	

class BarberAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'show_image', 'description')
	
	def show_image(self, obj):
		if obj.image:
			return mark_safe(
				'<img src="/media/{url}" width="auto" height="50" >'.format(
					url=obj.image.image.url.split("/media/")[-1])
			)


admin.site.register(Barber, BarberAdmin)
admin.site.register(BarberImage, BarberImageAdmin)
