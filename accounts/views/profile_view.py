from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import ProfileSerializer
from accounts.services.user_service import UserService


class ProfileView(GenericAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = ProfileSerializer

    def get(self, request):

        user = UserService.get_profile(
            request.user
        )

        serializer = self.get_serializer(
            user
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )