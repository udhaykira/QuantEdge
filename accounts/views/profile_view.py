from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import ProfileSerializer, ProfileUpdateSerializer
from accounts.services.user_service import UserService


class ProfileView(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = UserService.get_profile(
            request.user
        )

        serializer = ProfileSerializer(
            user
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
    
    def put(self,request):

        serializer = ProfileUpdateSerializer(instance = request.user,data = request.data)

        serializer.is_valid(
            raise_exception=True
        )

        user = UserService.update_profile(request.user, serializer.validated_data)

        response_serializer = ProfileUpdateSerializer(user)

        return Response(
            {
                "message": "Profile Updated Successfully",
                "user": response_serializer.data,
            },
            status = status.HTTP_200_OK,
        )
