from django.db import models
from django.contrib.auth.models import User

RIGHTS = (
    ('R', 'Read'),
    ('W', 'Write'),
    ('A', 'Admin'),
    ('O', 'Owner')
)

class Project(models.Model):
    name = models.CharField(max_length = 200)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"

class ACL(models.Model):
    project = models.ForeignKey('Project', related_name="users", related_query_name="user")
    person = models.ForeignKey(User)
    right = models.CharField(max_length = 1, choice = RIGHTS)

    def __str__(self):
        return self.title
