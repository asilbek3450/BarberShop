from django.db.models import Avg
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
		depth = 2
	
	@staticmethod
	def get_reviews(self):
		bookings = Booking.objects.filter(barber_id=self.id)
		reviews = bookings.values('id', 'user_id', 'review_id__review_text', 'created_at')
		return reviews
	
	@staticmethod
	def get_overall_rating(self):
		bookings = Booking.objects.filter(barber_id=self.id)
		overall_rating = bookings.aggregate(Avg('rate'))
		return overall_rating
