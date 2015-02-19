# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0004_auto_20150219_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='group',
            field=models.ForeignKey(default=1, to='banners.Group'),
            preserve_default=True,
        ),
    ]
