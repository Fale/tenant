from django.contrib import admin
from tenant.models import Tenant

class TenantAdmin(admin.ModelAdmin):
    fields =  ['name']

admin.site.register(Tenant)
