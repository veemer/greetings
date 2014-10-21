# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from greetings.models import Category, Greeting
from greetings.views import GreetingsList

# Create your tests here.

class TestViews(TestCase):

    def test_main_view(self):

        cat = Category.objects.create(name='test')
        for i in range(0, 50):
            g = Greeting(category=cat, text='test text')
            if i % 2:
                g.for_main = True
            g.save()

        url = reverse('main')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['is_top'])
        for greeting in response.context['greetings']:
            self.assertTrue(greeting.for_main)

        self.assertIn(cat, response.context['root_cats'])

    def test_child_category_view(self):
        
        root_cat = Category.objects.create(name='root cat 1')
        child_cats = []
        for i in range(0, 10):
            child_cats.append(Category.objects.create(name='cat {}'.format(i), parent=root_cat))

        url = reverse('child_categories', args=(root_cat.id,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        for cat in child_cats:
            self.assertIn(cat, response.context['child_cats'])
        
        self.assertIn(root_cat, response.context['root_cats'])

    def test_greetings_list_view(self):
        
        root_cat = Category.objects.create(name='root cat')
        child_cat = Category.objects.create(name='child cat', parent=root_cat)

        url = reverse('greetings', args=(child_cat.id,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        greetings = []
        for i in range(GreetingsList.paginate_by * 2, 0, -1):
            greetings.append(Greeting.objects.create(text='greeting {}'.format(i), category=child_cat, sort=i))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['greetings']), GreetingsList.paginate_by)

        for i in range(0, GreetingsList.paginate_by):
            self.assertEqual(response.context['greetings'][i], greetings[i])

        self.assertEqual(response.context['root_cat'], root_cat)
        self.assertIn(root_cat, response.context['root_cats'])
        self.assertEqual(response.context['child_cat'], child_cat)