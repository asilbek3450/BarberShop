from django.db import models


class Service(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	price = models.IntegerField()
	duration = models.IntegerField('duration (minut)', default=30)
	
	class Meta:
		ordering = ['-id']
	
	def __str__(self):
		return f'id-{self.id} {self.title}'
	

# Create your models here.
class ServiceImage(models.Model):
	image = models.ImageField(upload_to='service_images/')
	service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_images')

	class Meta:
		ordering = ['-id']

	def __str__(self):
		return f'Image of {self.service.title}, id-{self.id}'
	
	def save(self, *args, **kwargs):
		self.image.name = f'{self.service.title}.jpg'
		super().save(*args, **kwargs)
		