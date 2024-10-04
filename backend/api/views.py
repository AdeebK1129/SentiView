from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def hello_world(request):
    """
    Hello World API view.

    This view handles GET requests and returns a JSON response containing a 'Hello, World!' message.

    Example:
    - GET /api/hello/

    Returns:
        JsonResponse: A JSON response containing a message key:
        {
            "message": "Hello, world!"
        }

    """
    return JsonResponse({'message': 'Hello, world!'})
