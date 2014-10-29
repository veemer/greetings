# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from blog.models import Post


class PostAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':'20', 'style': 'width:95%'})},
    }

    list_display = ('title', 'date_create')
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
