from django.conf.urls import url
from . import views
# import views
app_name = 'nuistcis'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nuistcis/news_slider/$', views.news_slider, name='news_slider'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^news_create/$', views.news_create, name='news_create'),
    url(r'^programs_list/$', views.programs_list, name='programs_list'),
    url(r'^nuistcis/programs_listdetail/(?P<id>\d+)/$', views.programs_listdetail, name='programs_listdetail'),
    url(r'^news_list/$', views.news_list, name='news_list'),

    url(r'^nuistcis/about_list/(?P<id>\d+)/$', views.about_list, name='about_list'),
    url(r'^nuistcis/scholar_detail/(?P<id>\d+)/$', views.scholar_detail, name='scholar_detail'),
    url(r'^nuistcis/school_list/(?P<id>\d+)/$', views.school_list, name='school_list'),

    url(r'^news_slider/$', views.news_slider, name='news_slider'),
    url(r'^news_slider1/$', views.news_slider, name='news_slider1'),
    url(r'^nuistcis/(?P<id>\d+)/$', views.news_detail, name='news_detail'),
    url(r'^(?P<department_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<activity_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^activities/(?P<filter_by>[a-zA_Z]+)/$', views.activities, name='activities'),
    url(r'^create_department/$', views.create_department, name='create_department'),
    url(r'^(?P<department_id>[0-9]+)/create_activity/$', views.create_activity, name='create_activity'),
    url(r'^(?P<department_id>[0-9]+)/delete_activity/(?P<activity_id>[0-9]+)/$', views.delete_activity, name='delete_activity'),
    url(r'^(?P<department_id>[0-9]+)/favorite_department/$', views.favorite_department, name='favorite_department'),
    url(r'^(?P<department_id>[0-9]+)/delete_department/$', views.delete_department, name='delete_department'),
]
