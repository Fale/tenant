from django.db import models
from django.contrib.auth.models import User

RIGHTS = (
    ('K', 'Acknowledge'),
    ('R', 'Read'),
    ('C', 'Create'),
    ('E', 'Edit'),
    ('A', 'Admin'),
)

class Tenant(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    tenant = models.ForeignKey(Tenant)
    user = models.ForeignKey(User)
    rights = models.CharField(max_length = 1, choices = RIGHTS)
