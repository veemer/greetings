from django.conf.urls import patterns, include, url
from greetings.views import MainView, ChildCategoryView, GreetingsList

urlpatterns = patterns('',
    url(r'^$', MainView.as_view(), name='main'),
    url(r'categories/(?P<category_id>\d+)/$', ChildCategoryView.as_view(), name='child_categories'),
    url(r'greetings/(?P<category_id>\d+)/$', GreetingsList.as_view(), name='greetings'),
    url(r'greetings/(?P<category_id>\d+)/page(?P<page>\d+)/$', GreetingsList.as_view(), name='greetings'),
)
