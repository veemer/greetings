# -*- coding: utf-8 -*-

from django import template
from banners.models import Banner

register = template.Library()

@register.simple_tag
def banner(group_name='default'):

	banner = Banner.objects.filter(enabled=True, group__name=group_name).first()

	if banner:
		return banner.content
	else:
		return ''
