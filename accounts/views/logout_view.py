from rest_framework.generics import (
    GenericAPIView,
)

from rest_framework.response import (
    Response,
)

from rest_framework import status

from accounts.serializers import (
    LogoutSerializer,
)

from accounts.services.user_service import (
    UserService,
)


class LogoutView(
    GenericAPIView
):

    serializer_class = LogoutSerializer

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

        UserService.logout(

            serializer.validated_data[
                "refresh"
            ]

        )

        return Response(

            {

                "message":

                "Logout successful."

            },

            status=status.HTTP_200_OK,

        )