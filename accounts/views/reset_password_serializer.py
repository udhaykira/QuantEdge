from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.services.user_service import UserService
from accounts.serializers import ResetPasswordSerializer


class ResetPasswordView(
    GenericAPIView
):
    
    permission_classes = [IsAuthenticated]
    serializer_class = (
        ResetPasswordSerializer
    )

    def post(
        self,
        request,
    ):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        result = UserService.reset_password(
            request.user,
            serializer.validated_data,
        )

        if result == "phone_number":

            return Response(
                {
                    "message":
                    "Phone number is not registered."
                },
                status=400,
            )

        if result == "otp":

            return Response(
                {
                    "message":
                    "Invalid OTP."
                },
                status=400,
            )

        return Response(
            {
                "message":
                "Password reset successfully."
            },
            status=200,
        )