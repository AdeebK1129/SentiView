from django.db import models
from apps.core.abstracts.models import Timestamp
from apps.team.models import Team

class Review(Timestamp):
    """Model representing a review."""
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField()
    sentiment = models.CharField(
        max_length=20,
        choices=[('positive', 'Positive'), ('neutral', 'Neutral'), ('negative', 'Negative')]
    )
    problem_frequency = models.JSONField(default=dict)

class SentimentAnalysis(Timestamp):
    """Model for storing sentiment analysis results."""
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name="sentiment_analysis")
    positive_score = models.DecimalField(max_digits=3, decimal_places=2)
    neutral_score = models.DecimalField(max_digits=3, decimal_places=2)
    negative_score = models.DecimalField(max_digits=3, decimal_places=2)
