from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
	password = serializers.SerializerMethodField()
	
	class Meta:
		model = User
		fields = [
			'id',
			'name',
			'phone_number',
			'email',
			'password',
		]
		read_only_fields = [
			'id',
		]
	
	def get_password(self, obj):
		password = obj.phone_number
		return password
	