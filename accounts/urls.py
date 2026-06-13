from django.urls import path
from accounts.views import RegisterView, login, profile

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/',login,name='login'),
    path('profile/',profile,name="profile"),
]