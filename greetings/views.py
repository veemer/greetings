# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from greetings.models import Category, Greeting


class MainView(TemplateView):

    template_name = 'greetings/main.html'


class RootCategoryList(ListView):

    template_name = 'greetings/root_category_list.html'
    context_object_name = 'root_categories'
    model = Category

    def get_queryset(self):

        qs = super(RootCategoryList, self).get_queryset()
        return qs.filter(parent=None)


class ChildCategoryList(ListView):

    template_name = 'greetings/child_category_list.html'
    context_object_name = 'child_categories'
    model = Category

    def dispatch(self, request, *args, **kwargs):
        
        self.root_category = get_object_or_404(Category, pk=kwargs['category'])
        return super(ChildCategoryList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):

        qs = super(ChildCategoryList, self).get_queryset()
        return qs.filter(parent=self.root_category)

    def get_context_data(self, **kwargs):
        
        context = super(GreetingsList, self).get_context_data(**kwargs)
        context['root_cat'] = self.root_category

        return context


class GreetingsList(ListView):

    template_name = 'greetings/greetings_list.html'
    context_object_name = 'greetings'
    model = Greeting
    paginate_by = 40

    def dispatch(self, request, *args, **kwargs):
        
        self.category = get_object_or_404(Category, pk=kwargs['category'])
        return super(GreetingsList).dispatch(request, *args, **kwargs)

    def get_queryset(self):

        qs = super(GreetingsList, self).get_queryset()
        return qs.filter(category=self.category)

    def get_context_data(self, **kwargs):

        context = super(GreetingsList, self).get_context_data(**kwargs)
        context['current_cat'] = self.category
        context['root_cat'] = self.category.parent

        return context
