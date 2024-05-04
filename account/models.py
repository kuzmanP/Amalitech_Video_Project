from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        # Add this line to resolve the clash
        swappable = 'AUTH_USER_MODEL'


