import base64
#使用BASE64进行解码编码
# 编码
def encode():
    list_s = []
    r_move = int(2)
    s = 'test'
    s = s.encode()
    s = base64.b64encode(s)
    print("base64:{}".format(s))
    s = str(s)
    s = s[2:-1]
    print(s)
    for i in s:
        list_s.append(ord(i))
    for i in list_s:
        #       处理空格
        if i == 32:
            print(' ', end='')
        #       对大写字母进行处理
        elif 65 <= i <= 90:
            i += r_move
            while i > 90:
                i -= 26

        #       对小写字母进行处理
        elif 97 <= i <= 122:
            i += r_move
            while i > 122:
                i -= 26
        print(chr(i), end='') #6AQv5BaI6N6  6YOt5ZyG6L6 6YOt5ZyG6L6 6YOt5ZyG6L6J

def decode():   #解码函数
    l_move = 2
    s = '6AQv5BaI6N6L'
    list_s = []
    answer = ''
    for i in s:
        list_s.append(ord(i))
    for i in list_s:
        if i == 32:
            print(' ',end='')
        elif 65 <= i <= 90:
            i -= l_move
            while i < 65:
                i += 26
        elif 97 <= i <= 122:
            i -= l_move
            while i < 97:
                i += 26
        answer += chr(i)
    print(answer)
    b = bytes(answer, encoding='utf-8')
    print(b)
    res = base64.b64decode(b)
    print(res.decode())  # 默认以utf8解码
encode()

decode()
