from django.forms import ModelForm
from project.models import Project, ACL

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude=['owner']

class ACLForm(ModelForm):
    class Meta:
        model = ACL

