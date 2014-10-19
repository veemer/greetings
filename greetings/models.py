from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=128)
    parent = models.ForeignKey('Category', blank=True, null=True)

    def get_childs(self):
        return self.category_set.all().order_by('name')

    def __unicode__(self):
        return self.name


class Greeting(models.Model):

    category = models.ForeignKey(Category)
    text = models.TextField()
    for_main = models.BooleanField(default=False)
    from_pozdravok = models.BooleanField(default=False)
    sort = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text[:100]
