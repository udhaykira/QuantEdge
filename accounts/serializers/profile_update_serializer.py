from rest_framework import serializers
from accounts.models import User

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:

        model = User

        fields = (
            "username",
            "email",
            "phone_number",
        )

        extra_kwargs = {
            "username": {
                "required": True,
            },
            "email": {
                "required": True,
            },
            "phone_number": {
                "required": True,
            },
        }
    
    def validate_username(self, value):

        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Username cannot be empty."
            )

        return value

    def validate_email(self, value):

        if not value:
            raise serializers.ValidationError(
                "Email cannot be empty."
            )

        return value