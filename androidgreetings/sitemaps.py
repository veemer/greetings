# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap, GenericSitemap
from django.core.urlresolvers import reverse

from greetings.models import Category, Greeting
from blog.models import Post


class BaseSitemap(Sitemap):

	priority = 0.7

	def items(self):
		return ['main', 'posts_list']

	def location(self, item):
		return reverse(item)


root_dict = {
    'queryset': Category.objects.filter(parent__isnull=True)
}

child_dict = {
    'queryset': Category.objects.filter(parent__isnull=False)
}

posts_dict = {
    'queryset': Post.objects.all()
}

sitemaps = {
    'main': BaseSitemap,
    'root-cats': GenericSitemap(root_dict, priority=0.7),
    'greetings': GenericSitemap(child_dict, priority=0.7),
    'posts': GenericSitemap(posts_dict, priority=0.7),
}
