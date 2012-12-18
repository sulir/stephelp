from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    
    url(r'^projects/$', views.project_list, name='all-projects'),
    url(r'^projects/category/(?P<category_id>\d+)/$', views.project_list, name='category'),
    url(r'^projects/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='project'),
    url(r'^projects/add/$', views.ProjectCreate.as_view(), name='add-project'),
    url(r'^projects/(?P<pk>\d+)/edit/$', views.ProjectUpdate.as_view(), name='edit-project'),
    
    url(r'^tasks/project/(?P<project_id>\d+)/$', views.task_list, name='tasks'),
    url(r'^tasks/add/$', views.task_create, name='add-task'),
    url(r'^tasks/(?P<pk>\d+)/edit/$', views.task_update, name='edit-task'),
    url(r'^tasks/(?P<pk>\d+)/delete/$', views.task_delete, name='delete-task'),
    url(r'^tasks/(?P<pk>\d+)/support/$', views.task_support, name='support-task'),
    
    url(r'^users/(?P<user_id>\d+)/$', views.user_detail, name='user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
)