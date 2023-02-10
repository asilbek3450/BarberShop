from django.db import models

STATUS = (
	('pending', 'Kutilmoqda'),
	('accepted', 'Qabul qilindi'),
	('rejected', 'Bekor qilindi'),
	('done', 'Bajarildi'),
)

RATE = (
	(0, 0),
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
)


class Promocode(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	discount = models.IntegerField()
	start_date = models.DateField()
	end_date = models.DateField()
	is_active = models.BooleanField(default=True)
	
	class Meta:
		ordering = ['-id']
	
	def __str__(self):
		return f'{self.discount} %'


class Booking(models.Model):
	barber_id = models.ForeignKey('barbers.Barber', on_delete=models.SET_NULL, related_name='barber', null=True)
	user_id = models.ForeignKey('users.User', on_delete=models.SET_NULL, related_name='user', null=True)
	time = models.DateTimeField()
	status = models.CharField(choices=STATUS, max_length=100, default='pending')
	services = models.ManyToManyField('service.Service', related_name='services')
	comment = models.TextField(null=True, blank=True)
	review_id = models.ForeignKey('review.Review', on_delete=models.SET_NULL, related_name='review', null=True, blank=True)
	rate = models.IntegerField(choices=RATE, default=0)
	promocode_id = models.ForeignKey(Promocode, on_delete=models.SET_NULL, related_name='promocode', null=True, blank=True)
	
	created_at = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-id']
		
	def __str__(self):
		return f'{self.barber_id.name} - {self.user_id.name} - {self.time}'
	