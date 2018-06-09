from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^$', 'blog.views.home', name='home'), 
     url(r'^articles/$', 'blog.views.articles'),
     url(r'^get/(?P<article_id>\d+)/$', 'blog.views.article'), 
     url(r'^create/$', 'blog.views.create'),
     url(r'^edit/(?P<article_id>\d+)/$', 'blog.views.edit'), 
)

