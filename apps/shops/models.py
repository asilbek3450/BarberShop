from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(
	regex=r'^998[0-9]{9}$',
	message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)

TIME_CHOOSING = (
	('8 am', '8:00'),
	('9 am', '9:00'),
	('10 am', '10:00'),
	('11 am', '11:00'),
	('12 am', '12:00'),
	('1 pm', '13:00'),
	('2 pm', '14:00'),
	('3 pm', '15:00'),
	('4 pm', '16:00'),
	('5 pm', '17:00'),
	('6 pm', '18:00'),
	('7 pm', '19:00'),
	('8 pm', '20:00'),
	('9 pm', '21:00'),
	('10 pm', '22:00'),
	('11 pm', '23:00'),
	('12 pm', '24:00'),
)


class Shop(models.Model):  # for BarberShop
	title = models.CharField(max_length=100, blank=False, null=False, default=None)

	address = models.CharField(max_length=100, blank=False, null=False, default=None)
	latitude = models.DecimalField(max_digits=10, decimal_places=7, default=None)
	longitude = models.DecimalField(max_digits=10, decimal_places=7, default=None)
	
	# choose start and end time for work_time
	opening_hours = models.CharField(max_length=100, choices=TIME_CHOOSING, blank=False, null=False, default=None)
	closing_hours = models.CharField(max_length=100, choices=TIME_CHOOSING, blank=False, null=False, default=None)
	
	phone_number = models.CharField(max_length=12, validators=[phone_regex], blank=False, null=False, default=None)
	contact_link = models.URLField()  # telegram, instagram, facebook, etc.
	
	# reviews = models.JSONField(blank=True, null=True)  # reviews from users
	
	class Meta:
		ordering = ['-id']
	
	def __str__(self):
		return self.title + ' ' + self.phone_number
