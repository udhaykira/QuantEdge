from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status

from accounts.services.user_service import UserService
from accounts.serializers import RegisterSerializer

class RegisterView(GenericAPIView):
    """ This view is responsible for user registration """

    serializer_class = RegisterSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService.register(serializer.validated_data)
        response_serializer = RegisterSerializer(user)
        return Response(
            {
                'message':'User created successfully',
                'user':response_serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
