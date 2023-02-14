from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Service, ServiceImage


class ServiceImageAdmin(admin.ModelAdmin):
	list_display = [
		"id", "show_image", "service"
	]
	list_display_links = [
		"id", "service"
	]
	
	def show_image(self, obj):
		if obj.image:
			return mark_safe(
				'<img src="/media/{url}" width="auto" height="50" >'.format(
					url=obj.image.url.split("/media/")[-1])
			)


class ServiceAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'description', 'price', 'duration']


# Register your models here.
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceImage, ServiceImageAdmin)
