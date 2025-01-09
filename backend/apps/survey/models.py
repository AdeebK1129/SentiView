from django.db import models
from apps.core.abstracts.models import Timestamp
from apps.team.models import Team

class Survey(Timestamp):
    """Model representing a survey."""
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="surveys")
    title = models.CharField(max_length=255)
    description = models.TextField()

class SurveyResponse(Timestamp):
    """Model for survey responses."""
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="responses")
    response_data = models.JSONField()
