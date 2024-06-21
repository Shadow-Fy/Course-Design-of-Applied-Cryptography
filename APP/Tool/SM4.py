import binascii
from gmssl import sm4


def sm4_encode(key, data):
    """
    国密sm4加密
    :param key: 密钥
    :param data: 原始数据
    :return: 密文hex
    """
    sm4Alg = sm4.CryptSM4()  # 实例化sm4
    key_bytes = convert_key_to_bytes(key)
    sm4Alg.set_key(key_bytes, sm4.SM4_ENCRYPT)  # 设置密钥
    dateStr = str(data)
    # print("明文:", dateStr)
    enRes = sm4Alg.crypt_ecb(dateStr.encode())  # 开始加密,bytes类型，ecb模式
    enHexStr = enRes.hex()
    # print("密文:", enHexStr)
    return enHexStr  # 返回十六进制值


def convert_key_to_bytes(key):
    # 将数值转换为16字节的二进制数据
    key_bytes = key.to_bytes(16, byteorder='big')
    return key_bytes


def sm4_decode(key, data):
    """
    国密sm4解密
    :param key: 密钥
    :param data: 密文数据
    :return: 明文hex
    """
    sm4Alg = sm4.CryptSM4()  # 实例化sm4
    key_bytes = convert_key_to_bytes(key)
    sm4Alg.set_key(key_bytes, sm4.SM4_DECRYPT)  # 设置密钥
    deRes = sm4Alg.crypt_ecb(bytes.fromhex(data))  # 开始解密。十六进制类型,ecb模式
    deHexStr = deRes.decode()
    return deHexStr
