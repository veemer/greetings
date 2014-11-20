# -*- coding: utf-8 -*-

from django import template
from banners.models import Banner

register = template.Library()

@register.simple_tag
def banner():
	b = Banner.objects.filter(enabled=True).first()
	if b:
		return b.content
	else:
		return ''
