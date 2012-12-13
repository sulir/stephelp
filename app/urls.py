from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    url(r'^projects/$', views.project_list, name='all-projects'),
    url(r'^projects/category/(?P<category_id>\d+)/$', views.project_list, name='category'),
    url(r'^projects/(?P<pk>\d+)/$', views.ProjectDetail.as_view(), name='project'),
    url(r'^projects/create/$', views.ProjectCreate.as_view(), name='create-project'),
    url(r'^projects/(?P<pk>\d+)/update/$', views.ProjectUpdate.as_view(), name='update-project'),
    
    url(r'^users/(?P<user_id>\d+)/$', views.user_detail, name='user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    
    url(r'^about/$', views.about, name='about'),
)