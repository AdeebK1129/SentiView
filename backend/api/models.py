# api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any custom fields if needed in the future
    # Example:
    # company_name = models.CharField(max_length=255, blank=True, null=True)
    pass


