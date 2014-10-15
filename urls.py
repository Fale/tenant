from django.conf.urls import patterns, url
from .views import tenant

urlpatterns = patterns('',
    url(r'^$', tenant.list, name='listTenant'),
    url(r'^add/$', tenant.edit, name='addTenant'),
    url(r'^(?P<tenant_id>\d+)/$', tenant.show, name='showTenant'),
    url(r'^(?P<tenant_id>\d+)/edit/$', tenant.edit, name='editTenant'),
    url(r'^(?P<tenant_id>\d+)/delete/$', tenant.delete, name='deleteTenant'),
)
