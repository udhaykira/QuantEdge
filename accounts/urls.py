from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from accounts.views import (
        RegisterView,
        LoginView,
        ProfileView,
        ChangePasswordView,
        LogoutView,
    )

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('change-password/', ChangePasswordView.as_view(), name="change-password"),
    path('refresh-token/',TokenRefreshView.as_view()),
    path("logout/", LogoutView.as_view(), name="logout"),
]