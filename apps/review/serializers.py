from rest_framework import serializers

from apps.review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = (
			'id',
			'review_text',
			'user_id',
			'created_at',
		)
		read_only_fields = ('id',)
		depth = 1
		