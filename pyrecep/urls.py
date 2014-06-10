from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/consultas/', include('django_qbe.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',  include(admin.site.urls)),
)
