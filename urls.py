from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='listTenant'),
    url(r'^add/$', views.edit, name='addTenant'),
    url(r'^(?P<tenant_id>\d+)/$', view.show, name='showTenant'),
    url(r'^(?P<tenant_id>\d+)/edit/$', view.edit, name='editTenant'),
    url(r'^(?P<tenant_id>\d+)/delete/$', view.delete, name='deleteTenant'),
)
