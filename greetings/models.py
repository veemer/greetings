from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class GreetingManager(models.Manager):

    def get_queryset(self):
        return super(GreetingManager, self).get_queryset().order_by('-sort')


class Category(models.Model):

    name = models.CharField(max_length=128)
    parent = models.ForeignKey('Category', blank=True, null=True)

    def get_childs(self):
        return self.category_set.all().order_by('name')

    def get_absolute_url(self):
        if self.parent:
            return reverse('greetings', args=(self.id,))
        else:
            return reverse('child_categories', args=(self.id,))

    def __unicode__(self):
        return self.name


class Greeting(models.Model):

    category = models.ForeignKey(Category)
    text = models.TextField()
    for_main = models.BooleanField(default=False)
    from_pozdravok = models.BooleanField(default=False)
    sort = models.IntegerField(default=0)

    objects = GreetingManager()

    def __unicode__(self):
        return self.text[:100]
