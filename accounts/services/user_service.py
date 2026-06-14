from accounts.models import User
from django.contrib.auth import authenticate

class UserService:
    
    @staticmethod
    def register(data):
        user = User.objects.create_user(
            username = data["username"],
            password = data["password"],
            email = data["email"],
        )
        return user
    
    @staticmethod
    def login(data):
        user = authenticate(
            username = data["username"],
            password = data["password"],
        )

        return user

    @staticmethod
    def get_profile(user):
        return user
    