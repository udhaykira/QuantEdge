from rest_framework import serializers


class VerifyOTPSerializer(
    serializers.Serializer
):

    phone_number = serializers.CharField(
        write_only=True,
    )

    otp = serializers.CharField(
        write_only=True,
    )