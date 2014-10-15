from django.db import models
from django.contrib.auth.models import User

RIGHTS = (
    ('R', 'Read'),
    ('W', 'Write'),
    ('A', 'Admin'),
    ('O', 'Owner')
)

class Tenant(models.Model):
    name = models.CharField(max_length = 200)
    user = models.iManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name

class Membership(model.Model):
    tenant = models.ForeignKey(Tenant)
    user = models.ForeignKey(User)
    admin = models.BooleanField()
