from django.db import models


class BarberImage(models.Model):
	image = models.ImageField(upload_to='barbers_images/')
	
	class Meta:
		ordering = ['-id']
	
	def __str__(self):
		return f'id-{self.id}'


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
	