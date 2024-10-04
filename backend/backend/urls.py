from django.urls import path
from api.views import hello_world

# Define the URL routing for the API views
urlpatterns = [
    path('api/hello/', hello_world, name='hello_world'),
]
