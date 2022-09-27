from django.db import models

# Create your models here.
from django.db import models


class SessionType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=800, blank=True, null=True)

    def __str__(self):
        return self.name


class SessionStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=800, blank=True, null=True)

    def __str__(self):
        return self.name


class SessionReason(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=800, blank=True, null=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    type = models.ForeignKey(SessionType, on_delete=models.CASCADE)
    status = models.ForeignKey(SessionStatus, on_delete=models.CASCADE)
    reason = models.ManyToManyField(SessionReason, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
