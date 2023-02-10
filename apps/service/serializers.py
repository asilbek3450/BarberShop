from rest_framework import serializers

from apps.service.models import Service, ServiceImage


class ServiceImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ServiceImage
		fields = [
			'id',
			'image',
		]


class ServiceSerializer(serializers.ModelSerializer):
	images = serializers.SerializerMethodField()
	
	class Meta:
		model = Service
		fields = [
			'id',
			'title',
			'description',
			'price',
			'duration',
			'images',
		
		]
	
	def get_images(self):  # return images of service that service_id = ServiceImage.service_id
		images = ServiceImage.objects.filter(service_id=self.instance.id)
		return images
