# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_default_group(apps, schema_editor):

    Group = apps.get_model('banners', 'Group')
    Group.objects.create(name=u'default', id=1)


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0003_group'),
    ]

    operations = [
        migrations.RunPython(create_default_group),
    ]
