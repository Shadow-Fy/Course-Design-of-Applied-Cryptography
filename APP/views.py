from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def login(request):
    '''
    json格式
    {
        'username':''
        'password:''
    }
    :param request:
    :return:
    '''
    body = json.loads(request.body)
    return JsonResponse(
        {
            'data': '1111'
        }
    )
