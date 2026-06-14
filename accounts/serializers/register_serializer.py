from rest_framework import serializers

from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = (
            "username",
            "email",
            "password",
        )

        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 8,
            }
        }

    def validate_username(self, value):

        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Username cannot be empty."
            )

        if User.objects.filter(
            username=value
        ).exists():

            raise serializers.ValidationError(
                "Username already exists."
            )

        return value

    def validate_email(self, value):

        if User.objects.filter(
            email=value
        ).exists():

            raise serializers.ValidationError(
                "Email already exists."
            )

        return value

    def validate(self, attrs):

        if attrs.get("username") == attrs.get("password"):

            raise serializers.ValidationError(
                "Username and password cannot be same."
            )

        return attrs