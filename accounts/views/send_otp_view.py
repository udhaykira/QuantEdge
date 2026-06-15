from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from accounts.services.user_service import UserService
from accounts.serializers import SendOTPSerializer


class SendOTPView(
    GenericAPIView
):
    
    permission_classes = [IsAuthenticated]
    serializer_class = SendOTPSerializer

    def post(self, request,):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        UserService.send_otp(
            request.user,
            serializer.validated_data,
        )

        return Response(
            {
                "message":
                "OTP sent successfully."
            },
            status = status.HTTP_200_OK,
        )