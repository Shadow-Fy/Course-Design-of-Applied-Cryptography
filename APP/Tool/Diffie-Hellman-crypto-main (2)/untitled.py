# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):  #这个方法包含了用户界面的布局和控件的初始化设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditkey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditkey.setGeometry(QtCore.QRect(350, 20, 141, 31))
        self.lineEditkey.setObjectName("lineEditkey")
        self.pushButtonkey = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonkey.setGeometry(QtCore.QRect(510, 20, 81, 31))
        self.pushButtonkey.setObjectName("pushButtonkey")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 30, 161, 16))
        self.label.setObjectName("label")
        self.textEditalice = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditalice.setGeometry(QtCore.QRect(10, 120, 301, 231))
        self.textEditalice.setObjectName("textEditalice")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 91, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEditbob = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditbob.setGeometry(QtCore.QRect(410, 120, 301, 231))
        self.textEditbob.setObjectName("textEditbob")
        self.pushButtonalice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonalice.setGeometry(QtCore.QRect(210, 80, 81, 31))
        self.pushButtonalice.setObjectName("pushButtonalice")
        self.pushButtonbob = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonbob.setGeometry(QtCore.QRect(610, 80, 81, 31))
        self.pushButtonbob.setObjectName("pushButtonbob")
        self.lineEditalice = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditalice.setGeometry(QtCore.QRect(80, 80, 111, 31))
        self.lineEditalice.setObjectName("lineEditalice")
        self.lineEditbob = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditbob.setGeometry(QtCore.QRect(480, 80, 111, 31))
        self.lineEditbob.setObjectName("lineEditbob")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)  #这个方法用于设置界面上各个控件的文本内容，包括窗口标题、按钮文本等。
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):  #这是用户界面的描述类，包含了用户界面的布局和控件信息
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "diffie-hellman加密测试程序"))
        self.pushButtonkey.setText(_translate("MainWindow", "确定"))
        self.label.setText(_translate("MainWindow", "公共秘钥，必须为一个素数"))
        self.label_2.setText(_translate("MainWindow", "Alice"))
        self.label_3.setText(_translate("MainWindow", "Bob"))
        self.pushButtonalice.setText(_translate("MainWindow", "发送"))
        self.pushButtonbob.setText(_translate("MainWindow", "发送"))
