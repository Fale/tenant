from django.contrib import admin
from project.models import Project, ACL

class ProjectAdmin(admin.ModelAdmin):
    fields =  ['name']

admin.site.register(Project)
admin.site.register(ACL)
