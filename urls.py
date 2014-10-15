from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='listTenant'),
    url(r'^add/$', views.edit, name='addTenant'),
    url(r'^(?P<tenant_id>\d+)/$', views.show, name='showTenant'),
    url(r'^(?P<tenant_id>\d+)/edit/$', views.edit, name='editTenant'),
    url(r'^(?P<tenant_id>\d+)/delete/$', views.delete, name='deleteTenant'),
)
