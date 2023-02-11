from rest_framework import serializers

from apps.service.models import Service, ServiceImage


class ServiceImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ServiceImage
		fields = [
			'id',
			'image',
			'service',
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
	
	def get_images(self, obj):
		images = obj.service_images.all()
		serializer = ServiceImageSerializer(images, many=True)
		return serializer.data
	