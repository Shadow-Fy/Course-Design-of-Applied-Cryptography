from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from APP.Data.Info import userList, UserData, msgList
from APP.Tool import SM3


@csrf_exempt
def login(request):
    body = json.loads(request.body)
    username = body['username']
    password = body['password']
    for user in userList:
        if user.username == username:
            if user.password == SM3.sm3_hash(bytes(password, encoding='utf-8')):
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
                        "msg": f"密码错误"
                    }
                )
    return JsonResponse(
        {
            "code": -1,
            "msg": f"用户名或密码错误{username}"
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
        password = SM3.sm3_hash(str(password).encode('utf-8'))
        userList.append(UserData(username, password, '', '', '', ''))
        return JsonResponse({
            'code': 1,
            'msg': f'注册成功:\n账号为{username}\n密码为{password}',
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
    friend = body['friend']
    for user in userList:
        if user.username == username:
            for f in user.friendList:
                if f == friend:
                    return JsonResponse({
                        'code': -1,
                        'msg': '已有此好友'
                    })
            for use in userList:
                # 看是否有这个用户存在
                if use.username == friend:
                    use.friendList.append(user.username)
                    user.friendList.append(friend)
                    return JsonResponse({
                        'code': 1,
                        'msg': '添加成功'
                    })
            return JsonResponse({
                'code': -1,
                'msg': '查无此人'
            })
    return JsonResponse({
        'code': -1,
        'msg': '错误'
    })


@csrf_exempt
def updateFriend(request):
    body = json.loads(request.body)
    username = body['username']
    print("服务器收到好友列表更新信息" + username)
    for user in userList:
        if user.username == username:
            print("服务器返回user.friendList,username=" + user.username)
            return JsonResponse(user.friendList, safe=False)


@csrf_exempt
def sendMsg(request):
    '''
    json格式
    {
        'send':'发送者username'
        'recv‘:'接受者username'
        'msg':'发送内容’
    }
    :param request:
    :return:
    '''
    # 获取收到的信息
    body = json.loads(request.body)
    send = body['sendname']
    recv = body['recvname']
    msg = body['msg']
    msgList.append({
        'send': send,
        'recv': recv,
        'msg': msg
    })
    # 循环所有消息列表，如果有是发送给自己的信息，则返回
    for message in msgList:
        if message['recv'] == send:
            return JsonResponse({
                'msg': message['msg'],
            })


@csrf_exempt
def loopMsg(request):
    # 获取想获得轮询消息的人，将对应消息全部发送
    body = json.loads(request.body)
    send = body['sendname']
    for message in msgList:
        if message['recv'] == send:
            return JsonResponse({
                'msg': message['msg'],
            })
