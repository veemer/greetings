from django.conf.urls import patterns, include, url
from greetings.views import MainView, RootCategoryList, ChildCategoryList, GreetingsList

urlpatterns = patterns('',
    url(r'^$', MainView.as_view(), name='main'),
    url(r'categories/$', RootCategoryList.as_view(), name='root_categories'),
    url(r'categories/(?P<category_id>\d+)/$', ChildCategoryList.as_view(), name='child_categories'),
    url(r'categories/(?P<category_id>\d+)/greetings/$', GreetingsList.as_view(), name='greetings'),
    url(r'categories/(?P<category_id>\d+)/greetings/page(?P<page>\d+)/$', GreetingsList.as_view(), name='greetings'),
)
