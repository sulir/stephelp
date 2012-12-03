from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    
    url(r'^projects/$', project_list, name='all-projects'),
    url(r'^projects/category/(?P<category_id>\d+)/$', project_list, name='category'),
    url(r'^projects/(?P<project_id>\d+)/$', project_detail, name='project'),
    url(r'^projects/create/$', project_create, name='create-project'),
    url(r'^projects/(?P<project_id>\d+)/update/$', project_update, name='update-project'),
    
    url(r'^users/(?P<user_id>\d+)/$', user_detail, name='user'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    
    url(r'^about/$', about, name='about'),
)