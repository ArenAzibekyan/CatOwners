from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Cat(models.Model):
    name = models.CharField(max_length=200, unique=True)
    birthday = models.DateField(default=timezone.now())
    breed = models.CharField(max_length=200)
    hairiness = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)