# -*- coding: utf-8 -*-

from django.contrib import admin

from greetings.models import Category, Greeting


class RootCatsFilter(admin.SimpleListFilter):

    title = u'Categories'
    parameter_name = u'parent'

    def lookups(self, request, model_admin):
        cats = Category.objects.filter(parent__isnull=True)
        filters = [('root', 'Roots')]
        filters += [(cat.id, cat.name) for cat in cats]

        return filters

    def queryset(self, request, queryset):

        cat = self.value()

        if cat is None:
            return queryset

        if cat == 'root':
            return queryset.filter(parent__isnull=True)

        else:
            return queryset.filter(parent=cat)


class MainPageGreetingsFilter(admin.SimpleListFilter):

    title = 'Greetings'
    parameter_name = 'for_main'

    def lookups(self, request, model_admin):
        return (
            ('True', 'For main page'),
        )

    def queryset(self, request, queryset):

        for_main = self.value()

        if for_main == 'True':
            return queryset.filter(for_main=True)

        else:
            return queryset


class CategoryAdmin(admin.ModelAdmin):

    def greetings_link(category):
        return '<a href="/admin/greetings/greeting/?category__id__exact={}">Поздравления</a>'.format(category.id)
    greetings_link.allow_tags = True

    model = Category
    list_display = ('name', greetings_link)
    search_fields = ('name',)
    list_filter = (RootCatsFilter,)


class GreetingAdmin(admin.ModelAdmin):

    def teaser(self, greeting):
        return greeting.text[:100]

    model = Greeting
    list_display = ('teaser', 'category')
    list_filter = ('category', MainPageGreetingsFilter)
    search_fields = ('text',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Greeting, GreetingAdmin)
