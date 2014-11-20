# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Post
from greetings.views import BaseMixin, SeoMixin


class PostsList(BaseMixin, SeoMixin, ListView):

	model = Post
	per_page = 20
	template_name = 'blog/posts_list.html'
	context_object_name = 'posts'

	def get_h1(self):
		return u'Статьи к дню рождения'

	def get_title(self):
		return self.get_h1()

	def get_meta_description(self):
		return u'Интересные статьи о том как отпраздновать день рождения и что подарить близким'

	def get_meta_keywords(self):
		return u'статьи день рождения подарок как отпраздновать'


class PostDetail(BaseMixin, SeoMixin, DetailView):

	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'

	def get_h1(self):
		return self.object.title

	def get_title(self):
		return self.get_h1()
