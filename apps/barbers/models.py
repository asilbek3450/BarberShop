from django.db import models
from django.utils.safestring import mark_safe


class BarberImage(models.Model):
	image = models.ImageField(upload_to='barbers_images/')

	def __str__(self):
		return f'id-{self.id}'
	
	# save image with generated name
	def save(self, *args, **kwargs):
		self.image.name = f'barber.jpg'
		super().save(*args, **kwargs)


# https://codinggear.blog/how-to-show-image-in-django-admin/#register-the-model
# Create your models here.
class Barber(models.Model):
	name = models.CharField(max_length=100)
	image = models.OneToOneField(BarberImage, on_delete=models.SET_NULL, null=True, related_name='barber_image')
	description = models.TextField()
	shop_id = models.ForeignKey('shops.Shop', on_delete=models.SET_NULL, null=True, related_name='working_shop')
	
	# overall_rate = models.FloatField(default=0)
	# reviews = models.ManyToManyField('review.Review', related_name='barber_reviews')
	
	def __str__(self):
		return self.name
