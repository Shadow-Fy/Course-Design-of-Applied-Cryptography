import binascii
from gmssl import sm3


def sm3_hash(message: bytes):
    """
    国密sm3加密
    :param message: 消息值，bytes类型
    :return: 哈希值
    """

    msg_list = [i for i in message]
    hash_hex = sm3.sm3_hash(msg_list)
    return hash_hex

