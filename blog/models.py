# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField


class Post(models.Model):

    title = models.CharField(max_length=128)
    image = ImageField(upload_to='posts')
    preview_text = models.TextField()
    detail_text = models.TextField()
    date_create = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
    	return reverse('post_detail', args=(self.pk,))

    def __unicode__(self):
        return self.title
