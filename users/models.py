from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomManager


# Create your models here.
class UserModel(AbstractUser):
    email = models.CharField(max_length=256, unique=True)

    objects = CustomManager()

    REQUIRED_FIELDS = []

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
