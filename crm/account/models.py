from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):

    seller_id = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.username