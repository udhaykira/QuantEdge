from accounts.models import User

class UserService:
    
    @staticmethod
    def register(data):
        user = User.objects.create_user(
            username = data["username"],
            password = data["password"],
            email = data["email"],
        )
        return user