from datetime import datetime

from rest_framework import serializers

from apps.booking.models import Promocode, Booking


class PromocodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Promocode
		fields = '__all__'
	
	def to_representation(self, instance):
		repr = super().to_representation(instance)
		repr['start_date'] = instance.start_date.strftime('%Y-%m-%d')
		repr['end_date'] = instance.end_date.strftime('%Y-%m-%d')
		return repr
	

class BookingSerializer(serializers.ModelSerializer):
	total_price = serializers.SerializerMethodField()
	
	class Meta:
		model = Booking
		fields = [
			'id',
			'barber_id',
			'user_id',
			'time',
			'status',
			'services',
			'comment',
			'review_id',
			'promocode_id',
			'created_at',
			'total_price',
		]
		
		read_only_fields = ['id', 'created_at']
		# depth = 1
		
	@staticmethod
	def get_total_price(obj):  # return total price of booking services with promocode
		total_price = 0
		for service in obj.services.all():
			total_price += service.price
		if obj.promocode_id:
			total_price = total_price - (total_price * obj.promocode_id.discount / 100)
		return total_price
	
	# def create(self, validated_data):
	# 	string_time = validated_data['time']
	# 	my_time = datetime.strptime(string_time, '%Y-%m-%dT%H:%M:%S.%fZ')
	# 	validated_data['time'] = my_time
	# 	return Booking.objects.create(**validated_data)

	def to_representation(self, instance): # return time in string format
		repr = super().to_representation(instance)
		repr['time'] = instance.time.strftime('%Y-%m-%d %H:%M:%S')
		repr['created_at'] = instance.created_at.strftime('%Y-%m-%d %H:%M:%S')
		return repr
	