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
    
    @staticmethod
    def update_profile(user,data):

        if (user.phone_number != data["phone_number"]):
            user.is_verified = False

        user.username = data["username"]
        user.email = data["email"]
        user.phone_number = data["phone_number"]

        user.save()

        return user
    
    @staticmethod
    def change_password(user, data):
        if not user.check_password(
            data["current_password"]
        ):
            return False
        
        user.set_password(data["new_password"])
        user.save()
        
        return user
            
        