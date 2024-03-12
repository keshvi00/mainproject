from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUserr(AbstractUser):
    employee_id = models.CharField(max_length=100, unique=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)