from django.db import models
import uuid

# Create your models here.
class Subjects(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100, unique=True)
	
	user_id = models.ManyToManyField('users.Users', blank=True)

	def __str__(self):
	    return self.name