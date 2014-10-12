from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=128)
    parent = models.ForeignKey('Category', blank=True, null=True)


class Greeting(models.Model):

    category = models.ForeignKey(Category)
    text = models.TextField()
