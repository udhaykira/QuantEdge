from rest_framework import serializers

from accounts.models import User


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = (
            "id",
            "username",
            "email",
            "phone_number",
            "is_verified",
        )

        read_only_fields = (
            "id",
            "username",
            "email",
            "phone_number",
            "is_verified",
        )