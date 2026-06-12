from rest_framework import serializers
from accounts.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def validate_username(self,value):
        if len(value.strip())==0:
            raise serializers.ValidationError(
                "Username cannot be empty"
            )
        
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Username already exists"
            )
        
        return value
    
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists"
            )
        return value
    
    def validate(self,attrs):
        if attrs["username"] == attrs["password"]:
            raise serializers.ValidationError(
                "Username and Password cannot be same"
            )
        return attrs
