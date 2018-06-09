from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # website sections urls
	url(r'^$', 'main.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^robots/', include('robots.urls')),

    # user authentication urls
    url(r'^login/$',  'main.views.login'),
    url(r'^invalid/$',  'main.views.invalid'),
    url(r'^user/$',  'main.views.user_area'),
    url(r'^auth/$',  'main.views.auth_view'),    
    url(r'^logout/$', 'main.views.logout'),
    url(r'^register/$', 'main.views.register_user'),

)
