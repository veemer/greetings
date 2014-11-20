# -*- coding: utf-8 -*-

from django.contrib import admin
from banners.models import Banner

# Register your models here.


class BannerAdmin(admin.ModelAdmin):

	list_display = ('name', 'enabled')


admin.site.register(Banner, BannerAdmin)