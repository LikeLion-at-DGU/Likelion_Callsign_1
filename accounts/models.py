from django.db import models
from typing import Reversible
from atexit import register
from django.contrib.auth.models import User
from django.conf import settings


class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=10,null=True)
    sports = models.CharField(max_length=100,null=True)


# Create your models here.
