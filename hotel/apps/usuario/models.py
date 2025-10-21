from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuarios(AbstractUser):
    Telefono = models.CharField(max_length=20, blank=True, null=True)
    DNI = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self):
        return self.username
