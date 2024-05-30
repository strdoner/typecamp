from django.urls import path, re_path
from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^$', index, name='home'),
    re_path(r'^test', test, name='test'),
    re_path(r'^dict_load', dict_load, name='dict_load'),
    re_path(r'^stats_update', stats_update, name='stats_update'),
    re_path(r'^total_stats_update', total_stats_update, name='total_stats_update'),
    re_path(r'^game', game, name='game'),
    re_path(r'^custom', custom, name='custom'),
    re_path(r'^lessons', lessons, name='lessons'),
    re_path(r'^login/$', user_login, name='login'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^edit_profile/(?P<id>\d+)/$', edit_profile, name='edit_profile'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^profile/(?P<id>\d+)/$', user_detail, name='user_detail'),
    re_path(r'^total_stats/$', total_stats_detail, name='total_stats_detail'),
    re_path(r'^blog/$', blog_list, name='blog_list'),
    re_path(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        post_detail,
        name='post_detail'),
]
