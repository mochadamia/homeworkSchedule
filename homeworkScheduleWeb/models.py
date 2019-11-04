from django.contrib.auth.models import User
from django.db import models


class Class(models.Model):
    name = models.TextField(default='', null=False)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    name = models.TextField(default='', null=False)
    content = models.TextField(default='', null=False)
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE, null=False)


class Comment(models.Model):
    content = models.TextField(default='', null=False)
    assignment_id = models.ForeignKey('Assignment', models.CASCADE, null=False)
    class_id = models.ForeignKey('Class', models.CASCADE, null=False)
    # 1 is active, 0 is deleted
    status = models.CharField(max_length=1, default='1', null=False)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

