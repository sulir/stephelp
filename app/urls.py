from django.conf.urls import patterns, url, include
import views
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^login_view', views.login_view, name='login_view'),
    url(r'^logout_view', views.logout_view, name='logout_view'),
)