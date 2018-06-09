from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^$', 'robots.views.home', name='home'), 
     url(r'^all/$', 'robots.views.all'),
     url(r'^get/(?P<robot_id>\d+)/$', 'robots.views.single'), 
     url(r'^create/$', 'robots.views.create'),
     url(r'^edit/(?P<robot_id>\d+)/$', 'robots.views.edit'), 
)

