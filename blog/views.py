# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from django.contrib.comments.forms import CommentForm
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType

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


class PostDetail(BaseMixin, SeoMixin, DetailView, FormView):

	model = Post
	form_class = CommentForm
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super(PostDetail, self).dispatch(request, *args, **kwargs)

	def get(self, request ,*args, **kwargs):

		form = self.get_form(self.form_class)
		context = self.get_context_data(object=self.object, form=form)

		return self.render_to_response(context)

	def get_form(self, form_class):

		if self.request.method == 'POST':
			form = form_class(self.object, data=self.request.POST)
		else:
			form = form_class(self.object)

		form.base_fields['email'].required = False

		return form

	def form_valid(self, form):

		comment = form.get_comment_object()
		comment.save()

		return super(PostDetail, self).form_valid(form)

	def get_success_url(self):
		return reverse('post_detail', args=(self.object.id,))

	def get_h1(self):
		return self.object.title

	def get_title(self):
		return self.get_h1()

	def get_context_data(self, **kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)

		post_type = ContentType.objects.get_for_model(Post)
		comments = Comment.objects.filter(object_pk=self.object.pk, content_type=post_type)

		context['comments'] = comments

		return context
