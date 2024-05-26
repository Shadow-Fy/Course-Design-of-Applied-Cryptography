from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Data.Info import userList, UserData


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
    username = body['username']
    password = body['password']
    for user in userList:
        if user.username == username:
            if user.password == password:
                return JsonResponse(
                    {
                        "code": 1,
                        "msg": "登录成功",
                    }
                )
            else:
                return JsonResponse(
                    {
                        "code": -1,
                        "msg": "用户名或密码错误"
                    }
                )


@csrf_exempt
def register(request):
    body = json.loads(request.body)
    username = body['username']
    password = body['password']
    confirm_password = body['confirm_password']
    for user in userList:
        if user.username == username:
            return JsonResponse({
                'code': -1,
                'msg': '用户名已存在，请更换用户名',
            })
    if password == confirm_password:
        userList.append(UserData(username, password, '', '', '', ''))
        return JsonResponse({
            'code': 1,
            'msg': '注册成功',
        })
    else:
        return JsonResponse({
            'code': -1,
            'msg': '两次输入的密码不同',
        })


@csrf_exempt
def personInfo(request):
    body = json.loads(request.body)
    username = body['username']
    password = body['password']
    for user in userList:
        if user.username == username:
            if user.password == password:
                return JsonResponse(
                    {
                        "code": 1,
                        "msg": "身份正确",
                    }
                )
            else:
                return JsonResponse(
                    {
                        'code': -1,
                        'msg': '身份错误',
                    }
                )


@csrf_exempt
def updatePersonInfo(request):
    body = json.loads(request.body)
    username = body['username']
    password = body['password']
    for user in userList:
        if user.username == username:
            if user.password != password:
                return JsonResponse({
                    'code': -1,
                    'msg': '身份错误',
                })
            phonenumber = body['phonenumber']
            if user.phonenumber == phonenumber:
                return JsonResponse(
                    {
                        'code': -1,
                        'msg': '手机号重复，无法修改个人信息',
                    }
                )
            user.phonenumber = phonenumber
            user.nickname = body['nickname']
            user.sex = body['sex']
            user.age = body['age']
            return JsonResponse(
                {
                    'code': 1,
                    'msg': '信息已经成功修改',
                    'nickname': user.nickname,
                    'age': user.age,
                    'sex': user.sex,
                    'phonenumber': user.phonenumber,

                }
            )


@csrf_exempt
def addFriend(request):
    body = json.loads(request.body)
    username = body['username']
    for user in userList:
        if user.username == username:
            return JsonResponse({
                'code': -1,
                'msg': '身份错误',
            })
    return JsonResponse({
        'code': -1,
        'msg': '查无此人',
    })
