from django.db import models


# Create your models here.
class Review(models.Model):
	review_text = models.TextField()
	user_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_review')
	created_at = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['-id']
	
	def __str__(self):
		return str(self.id)
