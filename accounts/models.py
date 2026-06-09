from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import BaseModel
# Create your models here.

class User(AbstractUser, BaseModel):
    phone_number = models.CharField(max_length=15, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

