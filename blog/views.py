# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Post


class PostsList(ListView):

	model = Post
	per_page = 20
	template_name = 'blog/posts_list.html'
	context_object_name = 'posts'


class PostDetail(DetailView):

	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'
