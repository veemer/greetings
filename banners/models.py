from django.db import models

# Create your models here.


class Group(models.Model):

	name = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name


class Banner(models.Model):

	name = models.CharField(max_length=128)
	content = models.TextField()
	enabled = models.BooleanField(default=False)
	group = models.ForeignKey(Group, default=1)

	def __unicode__(self):
		return self.name
