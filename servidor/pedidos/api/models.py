from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    isTechnician = models.BooleanField(default=False)

    def __str__(self):
        return self.username
class Priority(models.Model):
    name = models.CharField(blank=True, max_length=255)

class Status(models.Model):
    current = models.TextField(blank=True, null = True)

class Priority(models.Model):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name

class Status(models.Model):
    current = models.TextField(blank=True, null = True)

    def __str__(self):
        return self.current

class Type(models.Model):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name

class Constancy(models.Model):
    description = models.TextField(blank=True, null=True)
    attachedFile = models.FileField(blank=True, null=True)
    finishDate = models.DateField(blank=True, null=True)

class System(models.Model):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(blank=True, max_length=255)
    system = models.ForeignKey(System, related_name = 'system', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name, self.system

class Requisition(models.Model):
    type = models.ForeignKey(Type, related_name = 'type', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(CustomUser, related_name = 'author', on_delete=models.CASCADE, blank=True, null=True)
    assignedTechnician = models.ForeignKey(CustomUser, related_name = 'assignedTechnician', blank=True, on_delete=models.CASCADE, null=True)
    subject = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    priority = models.ForeignKey(Priority, related_name = 'priority', on_delete=models.CASCADE, blank=True, null=True)
    affectedSystem = models.ForeignKey(System, related_name = 'affectedSystem', on_delete=models.CASCADE, blank=True, null=True)
    module = models.ForeignKey(Module, related_name = 'module', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    attachedFile = models.FileField(blank=True, null=True)
    constancy = models.ForeignKey(Constancy, related_name = 'constancy', on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(Status, related_name = 'status', on_delete=models.CASCADE, default = 1)

    def __str__(self):
        return self.subject
