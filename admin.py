from django.contrib import admin
from tenant.models import Tenant, Membership

class TenantAdmin(admin.ModelAdmin):
    fields =  ['name']

class MembershipAdmin(admin.ModelAdmin):
    fields =  ['name']

admin.site.register(Tenant)
admin.site.register(Membership)
