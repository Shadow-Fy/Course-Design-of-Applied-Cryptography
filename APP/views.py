from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        key_value = data.get('username')
        print('接收到的数据:', key_value)
        return HttpResponse(status=200)