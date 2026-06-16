from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.services.user_service import UserService
from accounts.serializers import VerifyOTPSerializer

class VerifyOTPView(GenericAPIView):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = (
        VerifyOTPSerializer
    )

    def post(self, request,):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        success = UserService.verify_otp(
            request.user,
            serializer.validated_data,
        )

        if not success:

            return Response(
                {
                    "message":
                    "Invalid OTP."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message":
                "Phone number verified successfully."
            },
            status = status.HTTP_200_OK
        )