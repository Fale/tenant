from django.forms import ModelForm
from tenant.models import Tenant

class TenantForm(ModelForm):
    class Meta:
        model = Tenant
        exclude=['user']
