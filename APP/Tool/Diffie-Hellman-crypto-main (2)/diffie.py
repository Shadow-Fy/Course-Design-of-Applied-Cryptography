#coding=utf-8

import math
import random


def judge_prime(p):         #用于获取给定素数 p 的所有原根
    # 素数的判断
    if p <= 1:
        return False
    i = 2
    while i * i <= p:
        if p % i == 0:
            return False
        i += 1
    return True


def get_generator(p):       #用于计算A和B根据私钥生成的计算数
    # 得到所有的原根
    a = 2
    list = []
    while a < p:
        flag = 1
        while flag != p:
            if (a ** flag) % p == 1:
                break
            flag += 1
        if flag == (p - 1):
            list.append(a)
        a += 1
    return list


# A，B得到各自的计算数        
def get_calculation(p, a, X):             #用于根据私钥和计算数计算A和B的密钥。
    Y = (a ** X) % p
    return Y


# A，B得到交换计算数后的密钥
def get_key(X, Y, p):
    key = (Y ** X) % p
    return key


if __name__ == "__main__":                             #提示用户输入一个素数，然后利用 judge_prime() 函数来检查输入的是否为素数，如果不是素数，则要求用户重新输入。
    # 得到规定的素数
    flag = False
    while flag == False:
        print('Please input your number(It must be a prime!): ', end='')
        p = input()
        p = int(p)
        flag = judge_prime(p)
    print(str(p) + ' is a prime! ')

    # 得到素数的一个原根
    list = get_generator(p)
    print(str(p) + ' 的一个原根为：', end='')
    print(list[-1])
    print('------------------------------------------------------------------------------')



    # 得到A的私钥
    XA = random.randint(0, p - 1)
    print('A随机生成的私钥为：%d' % XA)

    # 得到B的私钥
    XB = random.randint(0, p - 1)
    print('B随机生成的私钥为：%d' % XB)
    print('------------------------------------------------------------------------------')

    # 得待A的计算数
    YA = get_calculation(p, int(list[-1]), XA)
    print('A的计算数为：%d' % YA)

    # 得到B的计算数
    YB = get_calculation(p, int(list[-1]), XB)
    print('B的计算数为：%d' % YB)
    print('------------------------------------------------------------------------------')

    # 交换后A的密钥
    key_A = get_key(XA, YB, p)
    print('A的生成密钥为：%d' % key_A)

    # 交换后B的密钥
    key_B = get_key(XB, YA, p)
    print('B的生成密钥为：%d' % key_B)
    print('---------------------------True or False------------------------------------')

    print(key_A == key_B)     #这一行代码打印出A和B生成的密钥是否相同的布尔值
