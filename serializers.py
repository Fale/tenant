from rest_framework import serializers
from tenant.models import Tenant

class TenantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tenant
        fields = ('name')

