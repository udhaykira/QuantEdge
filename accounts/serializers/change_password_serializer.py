from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):

    current_password = serializers.CharField(
        write_only = True
    )
    new_password = serializers.CharField(
        write_only = True
    )
    confirm_password = serializers.CharField(
        write_only = True
    )

    def validate(self, attrs):
        if attrs["new_password"]!=attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "confirm_password":
                    "Passwords do not match."
                }
            )
        
        if (
            attrs["current_password"]
            == attrs["new_password"]
        ):
            raise serializers.ValidationError(
                {
                    "new_password":
                    "New password cannot be same as current password."
                }
            )

        return attrs