#coding=utf-8 
import base64   #用于编码和解码数据
import sys      #用于与 Python 解释器进行交互。
import datetime  #用于获取当前时间
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from untitled import Ui_MainWindow
import random



class admin_grasping(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.UI.pushButtonkey.clicked.connect(lambda :self.get_diffiekey())
        self.UI.pushButtonalice.clicked.connect(lambda: self.alice_sent())
        self.UI.pushButtonbob.clicked.connect(lambda: self.bob_sent())
        self.alice_console = self.UI.textEditalice
        self.bob_console = self.UI.textEditbob
        self.key = None



    def get_diffiekey(self):
        p = self.UI.lineEditkey.text()    #用户输入一个素数作为公共密钥 p。
        p = int(p)                
        flag = self.judge_prime(p)            #程序判断该数是否为素数。
        if flag == True:
            list = self.get_generator(p)
            self.key = list[-1]
            QMessageBox.information(self, '提示', '计算成功 目前公钥为：{}'.format(self.key), QMessageBox.Yes)
            self.XA = random.randint(0, p - 1)
            self.sent_alice_text("我随机生成的私钥为:{}".format(str(self.XA)))
            self.XB = random.randint(0, p - 1)
            self.sent_bob_text("我随机生成的私钥为:{}".format(str(self.XB)))
            self.YA = self.get_calculation(p, self.key, self.XA)
            self.sent_alice_text("我的计算数为:{}".format(str(self.YA)))
            self.YB = self.get_calculation(p, self.key, self.XB)
            self.sent_bob_text("我的计算数为:{}".format(str(self.YB)))
            self.sent_alice_text("收到Bob的计算数:{}".format(str(self.YB)))
            self.sent_bob_text("收到Alice的计算数:{}".format(str(self.YA)))
            self.key_A = self.get_key(self.XA, self.YB, p)
            self.sent_alice_text("我计算出的私钥为:{}".format(str(self.key_A)))
            self.key_B = self.get_key(self.XB, self.YA, p)
            self.sent_bob_text("我计算出的私钥为:{}".format(str(self.key_B)))
        else:
            QMessageBox.information(self, '提示', '计算失败，请确定输入的数为素数', QMessageBox.No)

    def alice_sent(self):       #实现了 Alice 和 Bob 发送消息的过程
        if self.key == None:
            QMessageBox.information(self, '提示', '请先计算私钥后再进行消息发送', QMessageBox.No)
        else:
            self.alicemsg = self.UI.lineEditalice.text()
            msg = '我发送的消息为：{}'.format(self.alicemsg)
            self.sent_alice_text(msg)
            ans = self.encode(self.alicemsg, self.key_A)
            msg = '加密后为：{}'.format(ans)
            self.sent_alice_text(msg)
            msg = '我接收的消息为：{}'.format(ans)
            self.sent_bob_text(msg)
            ans = self.decode(ans, self.key_B)
            msg = '解密后为：{}'.format(ans)
            self.sent_bob_text(msg)

    def bob_sent(self):         #实现了 Alice 和 Bob 发送消息的过程
        if self.key == None:
            QMessageBox.information(self, '提示', '请先计算私钥后再进行消息发送', QMessageBox.No)
        else:
            self.bobmsg = self.UI.lineEditbob.text()
            msg = '我发送的消息为：{}'.format(self.bobmsg)
            self.sent_bob_text(msg)
            ans = self.encode(self.bobmsg, self.key_A)
            msg = '加密后为：{}'.format(ans)
            self.sent_bob_text(msg)
            msg = '我接收的消息为：{}'.format(ans)
            self.sent_alice_text(msg)
            ans = self.decode(ans, self.key_A)
            msg = '解密后为：{}'.format(ans)
            self.sent_alice_text(msg)



    def sent_alice_text(self, strs):   
        #self 表示类的实例对象，在类的方法中使用 self 可以访问该实例对象的属性和方法。这个参数在 sent_alice_text() 和 sent_bob_text() 方法中使用，用于表示要在消息框中显示的文本消息。
        #strs用于表示要在消息框中显示的文本消息。
        str1 = self.alice_console.toPlainText()
        str1 += str(datetime.datetime.now())[11:-7] + ':  ' + strs + '\n'
        self.alice_console.setText(str1)
        self.alice_console.moveCursor(QTextCursor.End)

    def sent_bob_text(self, strs):
        str1 = self.bob_console.toPlainText()
        str1 += str(datetime.datetime.now())[11:-7] + ':  ' + strs + '\n'
        self.bob_console.setText(str1)
        self.bob_console.moveCursor(QTextCursor.End)

    def judge_prime(self, p):
        #表示一个素数，用作 Diffie-Hellman 密钥交换算法中的公共参数。用户需要在界面中输入一个素数作为公共密钥 p。
        # 素数的判断
        if p <= 2:
            return False
        i = 2
        while i * i <= p:
            if p % i == 0:
                return False
            i += 1
        return True

    def get_generator(self, p):
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

    def get_calculation(self, p, a, X):
        #a是原根
        #X是私钥
        Y = (a ** X) % p
        return Y

    def get_key(self, X, Y, p):
       #X：表示发送方（Alice 或 Bob）的私钥。
       #Y：表示接收方（Bob 或 Alice）的交换计算数。
       #p：表示公共的素数。
        key = (Y ** X) % p
        return key

    # 编码
    def encode(self, s, r_move):
        #表示要加密或解密的消息，即用户在界面中输入的文本。
        #r_move 和 l_move：这两个参数用于表示 Caesar 密码中的密钥偏移量。在消息加密和解密过程中，会使用这两个参数对字符进行移位操作。
        list_s = []
        r_move = int(r_move)
        s = str(s)
        s = s.encode()
        s = base64.b64encode(s)
        s = str(s)
        s = s[2:-1]
        print(s)
        answer = ''
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
            answer += chr(i)
        return answer

    def decode(self, s, l_move):
        l_move = int(l_move)
        s = str(s)
        list_s = []
        answer = ''
        for i in s:
            list_s.append(ord(i))
        for i in list_s:
            if i == 32:
                print(' ', end='')
            elif 65 <= i <= 90:
                i -= l_move
                while i < 65:
                    i += 26
            elif 97 <= i <= 122:
                i -= l_move
                while i < 97:
                    i += 26
            answer += chr(i)
        b = bytes(answer, encoding='utf-8')
        res = base64.b64decode(b)
        return res.decode()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = admin_grasping()
    mainWindow.show()
    sys.exit(app.exec_())