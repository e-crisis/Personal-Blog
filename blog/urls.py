from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/$', views.new_entry, name='post'),
    url(r'^(?P<blog_id>[0-9]+)/submit_edit/$', views.submit_edit_entry,
        name='submit_edit'),
    url(r'^(?P<blog_id>[0-9]+)/edit/$', views.edit_entry, name='edit'),

]
