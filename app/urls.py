from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    url(r'^projects/$', views.project_list, name='all-projects'),
    url(r'^projects/category/(?P<category_id>\d+)/$', views.project_list, name='category'),
    url(r'^projects/(?P<project_id>\d+)/$', views.project_detail, name='project'),
    url(r'^projects/create/$', views.project_create, name='create-project'),
    url(r'^projects/(?P<project_id>\d+)/update/$', views.project_update, name='update-project'),
    
    url(r'^users/(?P<user_id>\d+)/$', views.user_detail, name='user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    
    url(r'^about/$', views.about, name='about'),
)