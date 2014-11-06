# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from greetings.models import Category, Greeting


class SeoMixin(object):

    def get_h1(self):
        return ''

    def get_title(self):
        return ''

    def get_meta_description(self):
        return ''

    def get_meta_keywords(self):
        return ''

    def get_context_data(self, **kwargs):
        context = super(SeoMixin, self).get_context_data(**kwargs)
        context['h1_title'] = self.get_h1()
        context['title'] = self.get_title()
        context['meta_description'] = self.get_meta_description()
        context['meta_keywords'] = self.get_meta_keywords()

        return context


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


class MainView(BaseMixin, SeoMixin, ListView):

    template_name = 'greetings/greetings_list.html'
    context_object_name = 'greetings'
    model = Greeting
    paginate_by = 100

    def get_queryset(self):
        qs = super(MainView, self).get_queryset()
        return qs.filter(for_main=True)

    def get_context_data(self, **kwargs):

        context = super(MainView, self).get_context_data(**kwargs)
        context['is_top'] = True

        return context

    def get_h1(self):
        return u'Лучшие поздравления с днем рождения'

    def get_title(self):
        return self.get_h1()

    def get_meta_description(self):
        return u'Здесь вы cможете подобрать поздравления с днем рождения для родителей, второй половинке, коллегам по работе или друзьям'

    def get_meta_keywords(self):
        return u'поздравления день рождения лучшие'


class ChildCategoryView(BaseMixin, SeoMixin, TemplateView):

    template_name = 'greetings/child_categories.html'

    def dispatch(self, request, *args, **kwargs):
        response = super(ChildCategoryView, self).dispatch(request, *args, **kwargs)

        if self.child_cat:
            raise Http404

        return response

    def get_h1(self):
        return u'Поздравления \u2192 {}'.format(self.root_cat.name)

    def get_title(self):
        return u'Поздравления {}'.format(self.root_cat.name)

    def get_meta_description(self):
        return u'Поздравления с днем рождения {}'.format(self.root_cat.name)

    def get_meta_keywords(self):
        cats_names = [c.name for c in self.child_cats]
        cats = ' '.join(cats_names[:10])
        return u'поздравления день рождения {}'.format(cats)


class GreetingsList(BaseMixin, SeoMixin, ListView):

    template_name = 'greetings/greetings_list.html'
    context_object_name = 'greetings'
    model = Greeting
    paginate_by = 20

    def dispatch(self, request, *args, **kwargs):

        if int(self.kwargs.get('page', 0)) == 1:

            category = get_object_or_404(Category, pk=self.kwargs['category_id'], parent__isnull=False)
            redirect_url = reverse('greetings', args=(category.id,))
            return HttpResponseRedirect(redirect_url, status=301)

        else:
            return super(GreetingsList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):

        qs = super(GreetingsList, self).get_queryset()
        return qs.filter(category=self.child_cat)

    def get_h1(self):
        page = self.kwargs.get('page', 1)
        if page != 1:
            return u'Поздравления с днем рождения {} - страница {}'.format(self.child_cat.name, page)
        else:
            return u'Поздравления с днем рождения {}'.format(self.child_cat.name)

    def get_title(self):
        return self.get_h1()

    def get_meta_description(self):
        return u'Здесь вы сможете найти поздравления с днем рождения {}'.format(self.child_cat.name)

    def get_meta_keywords(self):
        return u'поздравления день рождения {}'.format(self.child_cat.name)
