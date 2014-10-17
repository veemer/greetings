# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from greetings.models import Category, Greeting


class BaseMixin(object):

    template_name = 'greetings/base.html'

    root_cat = None
    root_cats = None

    child_cat = None
    child_cats = None

    def dispatch(self, request, *args, **kwargs):

        category_id = kwargs.get('category_id', None)

        self.root_cats = Category.objects.filter(parent__isnull=True)

        if category_id:

            cat = get_object_or_404(Category, pk=category_id)

            if cat.parent:
                self.root_cat = cat.parent
                self.child_cat = cat
            else:
                self.root_cat = cat

            if self.root_cat:
                self.child_cats = self.root_cat.get_childs().order_by('name')

        return super(BaseMixin, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):

        context = super(BaseMixin, self).get_context_data(**kwargs)
        
        context['root_cat'] = self.root_cat
        context['root_cats'] = self.root_cats

        context['child_cat'] = self.child_cat
        context['child_cats'] = self.child_cats

        return context


class MainView(BaseMixin, ListView):

    template_name = 'greetings/base.html'
    context_object_name = 'greetings'
    model = Greeting
    paginate_by = 100

    def get_queryset(self):
        qs = super(MainView, self).get_queryset()
        return qs.filter(for_main=True)


class ChildCategoryView(BaseMixin, TemplateView):

    template_name = 'greetings/base.html'


class GreetingsList(BaseMixin, ListView):

    template_name = 'greetings/base.html'
    context_object_name = 'greetings'
    model = Greeting
    paginate_by = 20

    def get_queryset(self):

        qs = super(GreetingsList, self).get_queryset()
        return qs.filter(category=self.child_cat)
