from rest_framework import serializers

from apps.shops.models import Shop


class ShopSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shop
		fields = [
			'id',
			'title',
			'address',
			'latitude',
			'longitude',
			'opening_hours',
			'closing_hours',
			'phone_number',
			'contact_link',
		]
		read_only_fields = ('id',)

		
		