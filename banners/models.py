from django.db import models

# Create your models here.

class Banner(models.Model):

	name = models.CharField(max_length=128)
	content = models.TextField()
	enabled = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name
