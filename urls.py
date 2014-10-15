from django.conf.urls import patterns, url, include
from .views import api, tenant
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', api.TenantViewSet)


urlpatterns = patterns('',
    url(r'^$', tenant.list, name='listTenant'),
    url(r'^add/$', tenant.edit, name='addTenant'),
    url(r'^(?P<tenant_id>\d+)/$', tenant.show, name='showTenant'),
    url(r'^(?P<tenant_id>\d+)/edit/$', tenant.edit, name='editTenant'),
    url(r'^(?P<tenant_id>\d+)/delete/$', tenant.delete, name='deleteTenant'),

    # API
    url(r'^api/v0/tenant$', include(router.urls)),
)
