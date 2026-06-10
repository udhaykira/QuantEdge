from django.shortcuts import render
from accounts.services.user_service import UserService
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

    

