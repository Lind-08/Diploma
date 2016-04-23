# Create your models here.
from django.db import models


class NodesGroup(models.Model):
    name = models.CharField(max_length=50)


class Node(models.Model):
    ip_address = models.GenericIPAddressField()
    state = models.BooleanField()
    description = models.TextField(null=True)
    group = models.ForeignKey(NodesGroup, null=True)


class Task(models.Model):
    name = models.CharField(max_length=50)
    exec_time = models.DateTimeField()
    description = models.TextField(null=True)
    path = models.FilePathField()


class Category(models.Model):
    name = models.CharField(max_length=100)


class Template(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    path = models.FilePathField()
