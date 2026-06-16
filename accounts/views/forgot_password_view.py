from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.services.user_service import UserService
from accounts.serializers import ForgotPasswordSerializer

class ForgotPasswordView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ForgotPasswordSerializer

    def post(self, request):

        serializer = self.get_serializer(
            data = request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        result = UserService.forgot_password(
            request.user,
            request.data
        )

        if result == "phone_number":

            return Response(
                {
                    "message":
                    "Phone number is not registered."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if result == "verified":

            return Response(
                {
                    "message":
                    "Phone number is not verified."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message":
                "OTP sent successfully."
            },
            status=status.HTTP_200_OK,
        )

