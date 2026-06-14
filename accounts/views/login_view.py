from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import LoginSerializer
from accounts.services.user_service import UserService
from accounts.services.jwt_service import JWTService


class LoginView(GenericAPIView):
    """This view is responsible for user login."""

    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = UserService.login(
            serializer.validated_data
        )

        if user is None:
            return Response(
                {
                    "message": "Invalid Credentials"
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        tokens = JWTService.generate_tokens(user)

        return Response(
            {
                "message": "Login Successful",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
                "refresh": tokens["refresh"],
                "access": tokens["access"],
            },
            status=status.HTTP_200_OK,
        )