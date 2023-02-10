from rest_framework import serializers

from apps.barbers.models import BarberImage, Barber
from apps.booking.models import Booking


class BarberImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = BarberImage
		fields = [
			'id',
			'image',
		]
	

class BarberSerializer(serializers.ModelSerializer):
	overall_rating = serializers.SerializerMethodField()
	reviews = serializers.SerializerMethodField()
	
	class Meta:
		model = Barber
		fields = (
			'id',
			'name',
			'image',
			'overall_rating',
			'reviews',
		)
		read_only_fields = ('id',)
		depth = 1
	
	@staticmethod
	def get_reviews(self):
		bookings = Booking.objects.all()
		reviews = []
		for booking in bookings:
			if booking.review_id:
				if self.id == booking.barber_id:
					reviews.append(booking.review_id)
		# reviews = [booking.review_id for booking in obj.booking_set.all() if booking.review_id and self.id == booking.a_id]
		return reviews
	
	@staticmethod
	def get_overall_rating(self):
		bookings = Booking.objects.all()
		overall_rating = 0
		count = 0
		for booking in bookings:
			if booking.rate:
				overall_rating += booking.rate
				count += 1
		if count > 0:
			overall_rating = overall_rating / count
		return overall_rating
	
	# def create(self, validated_data):
	# 	return Barber.objects.create(**validated_data)
	#
	# def update(self, instance, validated_data):
	# 	instance.overall_rating = self.get_overall_rating(instance)
	# 	instance.save()
	# 	return instance
	
