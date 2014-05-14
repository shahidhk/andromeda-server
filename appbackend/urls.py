from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appbackend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^get$', 'data.views.get_data'),
    url(r'^api/', include('data.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
