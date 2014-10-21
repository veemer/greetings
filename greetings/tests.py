# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse

from greetings.models import Category, Greeting

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

