from django.db import models
from apps.core.abstracts.models import Timestamp
from apps.team.models import Team

class Notification(Timestamp):
    """Model for notifications."""
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    type = models.CharField(
        max_length=20,
        choices=[('email', 'Email'), ('dashboard', 'Dashboard'), ('push', 'Push')]
    )
