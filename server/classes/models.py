from django.db import models
import uuid


# Create your models here.
class Classes(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	number = models.IntegerField(unique=True)

	user_id = models.ManyToManyField('users.Users', blank=True)
	
	def __str__(self):
	    return str(self.number)