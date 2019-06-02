# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import *
from PyQt5.QtSql import *
from Login import db
from Login import message
global account
from Ui_StudentInfoCreate import Ui_Dialog
global Sflag
Sflag=0

class StudentInfoCreateDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, paccount=None, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(StudentInfoCreateDialog, self).__init__(parent)
        self.setupUi(self)
        
        global account
        account=paccount
        self.lineEdit.setText(account)
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_str, ok=QInputDialog.getText(self,'出生年月', '在此输入出生年月：1999-03-18',QLineEdit.Normal, '1999-03-18' )
        self.lineEdit_3.setText(my_str)
    
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_str, ok=QInputDialog.getText(self,'班级号', '在此输入班级号：041701',QLineEdit.Normal, '041701' )
        self.lineEdit_6.setText(my_str)
    
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_list=[]
        my_list.append('男')
        my_list.append('女')
        my_str,ok=QInputDialog.getItem(self, '性别', '请选择性别', my_list)
        self.lineEdit_4.setText(my_str)
    
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_str, ok=QInputDialog.getDouble(self,'成绩', '在此输入成绩', 0, 0, 100)
        print(my_str)
        self.lineEdit_8.setText(str(my_str))
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_str, ok=QInputDialog.getText(self,'学院号', '在此输入学院号：09',QLineEdit.Normal, '09' )
        self.lineEdit_7.setText(my_str)
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        import re
        l1=account
        l2=self.lineEdit_2.text()
        l3=self.lineEdit_3.text()
        #判断日期输入格式
        if (re.search(r"(\d{4}-\d{1,2}-\d{1,2})", l3))and((len(l3)>=8)and(len(l3)<=10)):
            print(u"日期输入正确")
        else:
            message(u"错误", u"日期输入错误！请重新输入")
            self.lineEdit_3.setText("")
        l4=self.lineEdit_4.text()
        #判断性别输入格式
        if (re.search(r"男|女",l4))and(len(l4)==1)and(len(l4)==1):
            print(u"性别输入正确")
        else:
            message(u"错误", u"性别输入错误！请重新输入")
            self.lineEdit_4.setText("")
        l5=self.lineEdit_5.text()
        #判断手机号码输入格式
        if (re.search(r"\d{11}", l5))and(len(l5)==11):
            print(u"手机号码输入正确")
        else:
            message(u"错误",u"手机号错误，应为11位数字！请重新输入" )
            self.lineEdit_5.setText("")
        l6=self.lineEdit_6.text()
        #判断班级号输入格式
        if (re.search(r"\d{6}", l6))and(len(l6)==6):
            print(u"班级号输入正确")
        else:
            message(u"错误",u"班级号错误，应为6位数字！请重新输入" )
            self.lineEdit_6.setText("")
        l7=self.lineEdit_7.text()
        #判断学院号输入格式
        if (re.search(r"\d{2}", l7))and(len(l7)==2):
            print(u"学院号输入正确")
        else:
            message(u"错误",u"学院号错误，应为2位数字！请重新输入" )
            self.lineEdit_7.setText("")
        l8=self.lineEdit_8.text()
        #所有数据均输入正确
        if((l1!="")and(l2!="")and(l3!="")and(l4!="")and(l5!="")and(l6!="")and(l7!="")and(l8!="")):
            query = QSqlQuery(db)
            query.prepare("\
            insert into Student(Sno,Sname,Sbirth,Ssex,Sphone,ClassNo,SchoolNo,Sgrade)\
            values('{}','{}','{}','{}','{}','{}','{}','{}')\
            ".format(l1, l2, l3, l4, l5, l6, l7, l8))
            print("\
            insert into Student(Sno,Sname,Sbirth,Ssex,Sphone,ClassNo,SchoolNo,Sgrade)\
            values('{}','{}','{}','{}','{}','{}','{}','{}')\
            ".format(l1, l2, l3, l4, l5, l6, l7, l8))
            if query.exec():
                message(u"成功",u"插入用户成功" )
                global Sflag
                Sflag=1
            else:
                message1=QMessageBox()
                message1.setText(u"创建用户,请输入正确的学院号和班级号如左图所示,或者为输入了重复的学号，请退出重试")
                message1.setWindowTitle(u"错误")
                message1.setIconPixmap(QPixmap("Class.png"))
                message1.exec_()
        else:
            message(u"错误", u"请将数据填完整")
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
    
