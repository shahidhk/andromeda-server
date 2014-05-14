from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appbackend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^kadai/?$', 'data.views.get_kadai'),
    url(r'^kadai/(?P<kadai_id>\d+)$', 'data.views.get_kadai'),
)
