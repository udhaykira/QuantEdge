from django.shortcuts import render
from accounts.services.user_service import UserService
from accounts.services.jwt_service import JWTService
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def register(request):

    if request.method!='POST':
        return JsonResponse(
            {
                'message':'Invalid Request Method'
            },
            status=405,
        )
    
    data = json.loads(request.body)
    user = UserService.register(data)
    return JsonResponse(
        {
            'message':'User created successfully',
            'id':user.id,
        },
        status=201,
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
            "access":tokens["refresh"]
        },
        status=200
    )
    

