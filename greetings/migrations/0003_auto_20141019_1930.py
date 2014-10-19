# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greetings', '0002_greeting_for_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='greeting',
            name='from_pozdravok',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='greeting',
            name='sort',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
