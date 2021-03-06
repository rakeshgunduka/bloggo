from django.conf.urls import url,include
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	homepage,
	aboutpage,
	postpage,
	contactpage,
    suc,
	) 

urlpatterns = [
    url(r'^$',homepage,name='home'),
    url(r'^about/$',aboutpage,name='about'),
    url(r'^post/$',postpage,name='post'),
    url(r'^contact/$',contactpage,name='contact'),
    url(r'^create/$',post_create,name="create"),
    url(r'^list/$',post_list,name='list'),
    #url(r'^create/$',post_create),
    url(r'^(?P<user_id>\d+)/$',postpage,name='detail'),
    #url(r'^(?P<user_id>\d+)/$',post_detail,name='detail'),
    url(r'^(?P<user_id>\d+)/edit$',post_update,name='update'),
    url(r'^(?P<user_id>\d+)/delete$',post_delete),
    url(r'^success/',suc,name="success"),
]