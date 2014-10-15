from django.conf.urls import patterns, url
from .views import project

urlpatterns = patterns('',
    url(r'^$', project.list, name='listProject'),
    url(r'^add/$', project.edit, name='addProject'),
    url(r'^(?P<project_id>\d+)/$', project.show, name='showProject'),
    url(r'^(?P<project_id>\d+)/edit/$', project.edit, name='editProject'),
    url(r'^(?P<project_id>\d+)/delete/$', project.delete, name='deleteProject'),
)
