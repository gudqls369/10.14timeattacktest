from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    class Meta:
        db_table = "user" 

    phone = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)