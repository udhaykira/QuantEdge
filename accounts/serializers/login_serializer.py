from rest_framework import serializers


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField(
        write_only=True
    )

    def validate_username(self, value):

        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Username cannot be empty."
            )

        return value

    def validate_password(self, value):

        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Password cannot be empty."
            )

        return value