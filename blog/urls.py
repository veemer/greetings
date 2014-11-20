from django.conf.urls import patterns, include, url
from blog.views import PostsList, PostDetail

urlpatterns = patterns('',
    url(r'^$', PostsList.as_view(), name='posts_list'),
    url(r'(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
)
