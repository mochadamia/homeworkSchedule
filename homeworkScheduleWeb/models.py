from django.db import models


class ClassCategory(models.Model):
    name = models.TextField()


class Assignment(models.Model):
    name = models.TextField()
    content = models.TextField()
    class_id = models.ForeignKey('ClassCategory', models.CASCADE, null=False)


class Comment(models.Model):
    content = models.TextField()
    assignment_id = models.ForeignKey('Assignment', models.CASCADE, null=False)
    class_id = models.ForeignKey('ClassCategory', models.CASCADE, null=False)
    status = models.CharField(max_length=1)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    user_type = models.CharField(max_length=1, default='')
