from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.services.user_service import UserService
from accounts.serializers import ChangePasswordSerializer

class ChangePasswordView(GenericAPIView):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = (
        ChangePasswordSerializer
    )

    def post(self, request):

        serializer = self.get_serializer(data = request.data)

        serializer.is_valid(
            raise_exception=True,
        )

        success = UserService.change_password(
            request.user,
            serializer.validated_data,
        )

        if not success:
            return Response(
                {
                    "message":
                    "Current password is incorrect."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        return Response(
            {
                "message":
                "Password changed successfully."
            },
            status=status.HTTP_200_OK,
        )

