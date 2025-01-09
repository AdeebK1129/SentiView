from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from .models import User
from .serializers import UserSerializer, UserCreateSerializer


class UserCreateView(CreateAPIView):
    """
    API view for user registration.
    """
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        """
        Overriding create to include the `UserSerializer` in response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # Return the serialized user data with timestamps
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )



class UserProfileView(RetrieveUpdateAPIView):
    """
    API view for retrieving and updating user profile.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        return self.request.user


class ObtainAuthTokenView(APIView):
    def post(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate

        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=400)

        user = authenticate(request, email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": UserSerializer(user).data})
        return Response({"error": "Invalid credentials."}, status=401)



class UserLogoutView(APIView):
    """
    API view for user logout.
    Deletes the authentication token for the logged-in user.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Token not found."}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    """
    API view for changing user password.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        if not current_password or not new_password:
            return Response({"error": "Current and new passwords are required."}, status=400)

        user = request.user
        if not user.check_password(current_password):
            return Response({"error": "Current password is incorrect."}, status=401)

        user.set_password(new_password)
        user.save()
        return Response({"message": "Password updated successfully."}, status=200)


class ListAllUsersView(ListAPIView):
    """
    API view for listing all users.
    (Superuser-only functionality)
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Check if the user is a superuser
        if not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to view this resource.")
        return super().get_queryset()
