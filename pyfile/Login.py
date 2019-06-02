# -*- coding: utf-8 -*-

"""
Module implementing LoginDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets  import *
from PyQt5 import *

from Ui_Login import Ui_Dialog

from PyQt5. QtGui import  *
from PyQt5.QtSql import *
db = QSqlDatabase.addDatabase('QODBC')
db.setHostName('DESKTOP-8ITEMSI')
db.setDatabaseName('QTDSN')
#用于判断用户是否登录成功
flag=0
#用于判断用户类型
role="学生"
class LoginDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Treetog-I-Documents.ico"))
        self.setWindowIcon(icon)
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("on_pushButton_3_clicked")
        my_list=[]
        my_list.append('学生')
        my_list.append('教师')
        my_list.append('管理员')
        my_str,ok=QInputDialog.getItem(self, '用户类型', '请选择用户类型', my_list)
        self.lineEdit_3.setText(my_str)
        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        global account
        account=self.lineEdit.text()
        #对密码进行修正
        global role
        role=self.lineEdit_3.text()
        if role=="学生":
            cor='a'
        elif role=="教师":
            cor='b'
        else :
            cor='c'
        password=self.lineEdit_2.text()+cor

        print(account+password+role)
        db.setUserName(account)
        db.setPassword(password)
        
        if db.open():
            self.close()
            #登陆成功，flag变为1
            global flag
            flag=1
        else:
            message(u"错误", u"用户名或密码或用户类型输入错误！请重新输入")

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()
        
def message(title, str):
    message=QMessageBox()
    message.setText(str)
    message.setWindowTitle(title)
    message.exec_()
