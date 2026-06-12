from django.shortcuts import render
from accounts.services.user_service import UserService
from accounts.services.jwt_service import JWTService
from accounts.serializers.user_serializer import RegisterSerializer
from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@api_view(["POST"])
def register(request):
    
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = UserService.register(serializer.validated_data)
    return JsonResponse(
        {
            'message':'User created successfully',
            'id':user.id,
        },
        status=status.HTTP_201_CREATED,
    )

@csrf_exempt
def login(request):
    
    if request.method!="POST":
        return JsonResponse(
            {
                'message':'Invalid Request Method'
            },
            status=405,
        )
    
    data = json.loads(request.body)
    user = UserService.login(data)
    if user is None:
        return JsonResponse(
            {
            "message":"Invalid Credentials"
            },
            status=401
        )
    tokens = JWTService.generate_tokens(user)
    return JsonResponse(
        {
            "message":"Login Successful",
            "user":{
                "id":user.id,
                "username":user.username,
                "email":user.email,

            },
            "refresh":tokens["refresh"],
            "access":tokens["access"]
        },
        status=200
    )

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    data = UserService.get_profile(request.user)
    return Response(
        data,
        status=200,
    )

    

