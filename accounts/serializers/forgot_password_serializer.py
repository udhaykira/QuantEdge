from rest_framework import serializers


class ForgotPasswordSerializer(
    serializers.Serializer
):

    phone_number = serializers.CharField()

    def validate_phone_number(
        self,
        value,
    ):

        value = value.strip()

        if len(value) != 10:
            raise serializers.ValidationError(
                "Invalid Phone Number."
            )

        return value