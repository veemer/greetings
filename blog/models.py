# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models

from sorl.thumbnail import ImageField


class Post(models.Model):

    title = models.CharField(max_length=128)
    image = ImageField(upload_to='posts')
    preview_text = models.TextField()
    detail_text = models.TextField()
    date_create = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.title
