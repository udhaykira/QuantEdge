from rest_framework import serializers


class ResetPasswordSerializer(
    serializers.Serializer
):

    phone_number = serializers.CharField()

    otp = serializers.CharField()

    new_password = serializers.CharField(
        write_only=True,
    )

    confirm_password = serializers.CharField(
        write_only=True,
    )

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

    def validate(self, attrs):

        if (
            attrs["new_password"]
            !=
            attrs["confirm_password"]
        ):
            raise serializers.ValidationError(
                {
                    "confirm_password":
                    "Passwords do not match."
                }
            )

        return attrs