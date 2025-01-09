from django.db import models
from apps.core.abstracts.models import Timestamp
from apps.user.models import User

class Team(Timestamp):
    """Model representing a team."""
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_teams")

    def __str__(self):
        return self.name

class TeamMembership(Timestamp):
    """Model representing membership roles in a team."""
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="memberships")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_memberships")
    role = models.CharField(
        max_length=20,
        choices=[
            ('owner', 'Owner'),
            ('editor', 'Editor'),
            ('viewer', 'Viewer')
        ]
    )
