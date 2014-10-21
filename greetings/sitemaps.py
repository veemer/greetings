# -*- coding: utf-8 -*-

from django.contrib.sitemaps import GenericSitemap
from greetings.models import Category, Greeting

root_dict = {
    'queryset': Category.objects.filter(parent__isnull=True)
}

child_dict = {
    'queryset': Category.objects.filter(parent__isnull=False)
}

sitemaps = {
    'root-cats': GenericSitemap(root_dict, priority=0.7),
    'greetings': GenericSitemap(child_dict, priority=0.7),
}
