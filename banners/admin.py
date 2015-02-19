# -*- coding: utf-8 -*-

from django.contrib import admin
from banners.models import Banner, Group

# Register your models here.


class BannerAdmin(admin.ModelAdmin):

	list_display = ('name', 'enabled', 'group')


admin.site.register(Banner, BannerAdmin)
admin.site.register(Group)