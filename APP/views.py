from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from APP.Data.Info import userList, UserData, UserKeys, MessageData
from APP.Tool import SM3, diffie


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
                    privateKey = diffie.getPrivateKey()
                    use.userKeyList.append(UserKeys(user.username, privateKey))
                    user.userKeyList.append(UserKeys(use.username, privateKey))
                    use.friendList.append(user.username)
                    user.friendList.append(friend)
                    return JsonResponse({
                        'code': 1,
                        'msg': '添加成功',
                        'privateKey': privateKey
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
    print("服务器收到用户 {" + username + "} 好友列表更新信息")
    for user in userList:
        if user.username == username:
            print("服务器返回user.friendList,username=" + user.username)
            return JsonResponse(user.friendList, safe=False)


@csrf_exempt
def sendMsg(request):
    # 获取收到的信息
    body = json.loads(request.body)
    send = body['sendname']
    recv = body['recvname']
    msg = body['msg']
    sm3_msg = body['sm3_msg']
    send_time = body['send_time']
    for user in userList:
        if user.username == recv:
            user.msgList.append(MessageData(send, msg, sm3_msg, send_time))
            print(send + '）发送的信息已经存储在（' + recv + '）的消息列表中')
            return JsonResponse({
                'code': '1',
                'msg': '发送成功'
            })


@csrf_exempt
def get_image(request):
    body = json.loads(request.body)
    username = body['username']
    print("服务器收到用户 {" + username + "} 的消息更新请求")
    for user in userList:
        if user.username == username:
            if user.msgList:
                msg_list = [msg.to_dict() for msg in user.msgList]
            else:
                msg_list = []
            return JsonResponse(msg_list, safe=False)


@csrf_exempt
def msg_clean(request):
    body = json.loads(request.body)
    sendUser = body['sendUser']
    username = body['username']
    for user in userList:
        if user.username == username:
            user.remove_message_by_sender(sendUser)
            return JsonResponse({
                'code': '1',
                'msg': '清楚成功'
            })


@csrf_exempt
def updateUserData(request):
    body = json.loads(request.body)
    username = body['username']
    for user in userList:
        if user.username == username:
            user_data_dict = user.to_dict()
            return JsonResponse(user_data_dict)
