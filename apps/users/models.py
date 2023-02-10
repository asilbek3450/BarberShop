from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(
	regex=r'^998[0-9]{9}$',
	message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100, blank=False, null=False, default=None)
	phone_number = models.CharField(max_length=12, validators=[phone_regex], blank=False, null=False, default=None)
	email = models.EmailField(max_length=100, blank=True, null=True, default=None)

	class Meta:
		ordering = ['-id']
		
	def __str__(self):
		return self.name
	
	# REQUIRED_FIELDS = ['name', 'phone_number']
	# USERNAME_FIELD = 'name'
	