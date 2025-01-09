from django.urls import path
from .views import (
    UserCreateView,
    UserProfileView,
    ObtainAuthTokenView,
    UserLogoutView,
    ChangePasswordView,
    ListAllUsersView,
)

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='user-signup'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('login/', ObtainAuthTokenView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('all-users/', ListAllUsersView.as_view(), name='all-users'),
]
