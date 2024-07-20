class UserData:
    def __init__(self, username, password, nikename, age, sex, phonenumber):
        self.username = username
        self.password = password
        self.nikename = nikename
        self.age = age
        self.sex = sex
        self.phonenumber = phonenumber
        self.friendList = []
        self.userKeyList = []
        self.msgList = []

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'nikename': self.nikename,
            'age': self.age,
            'sex': self.sex,
            'phonenumber': self.phonenumber,
            'friendList': self.friendList,
            'userKeyList': [key.to_dict() for key in self.userKeyList],
            'msgList': [msg.to_dict() for msg in self.msgList]
        }

    def remove_message_by_sender(self, sendUser):
        self.msgList = [msg for msg in self.msgList if msg.sendUser != sendUser]


class UserKeys:
    def __init__(self, friendUser, private_key):
        self.friendUser = friendUser
        self.private_key = private_key

    def to_dict(self):
        return {
            'friendUser': self.friendUser,
            'private_key': self.private_key
        }


class MessageData:
    def __init__(self, sendUser, msg, sm3_msg, send_time):
        self.sendUser = sendUser
        self.msg = msg
        self.sm3_msg = sm3_msg
        self.send_time = send_time

    def to_dict(self):
        return {
            'sendUser': self.sendUser,
            'msg': self.msg,
            'sm3_msg': self.sm3_msg,
            'send_time': self.send_time
        }


userList = []
userList.append(UserData("111111", "c7f66beee198fb411c8623e53cbbc6eb1e0f078b5d68ed7f10d02ffb0af46d44", "", "", "", ""))
