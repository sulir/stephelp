from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stephelp.views.home', name='home'),
    # url(r'^stephelp/', include('stephelp.foo.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
