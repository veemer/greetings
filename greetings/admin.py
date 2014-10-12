from django.contrib import admin

from greetings.models import Category, Greeting


class CategoryAdmin(admin.ModelAdmin):

    model = Category


class GreetingAdmin(admin.ModelAdmin):

    def teaser(self, greeting):
        return greeting.text[:100]

    model = Greeting
    list_display = ('id', 'category', 'teaser')
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Greeting, GreetingAdmin)
