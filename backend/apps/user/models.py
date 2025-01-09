from django.db import models
from apps.core.abstracts.models import Timestamp

class User(Timestamp):
    """Model representing a user with optional demographic data."""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=20,
        choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
            ('prefer_not_to_say', 'Prefer not to say')
        ],
        blank=True,
        null=True
    )
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email
