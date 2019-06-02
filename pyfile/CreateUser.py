# -*- coding: utf-8 -*-

"""
Module implementing CreateUserDialog.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from StudentInfoCreate import  StudentInfoCreateDialog
from TeacherInfoCreate import TeacherInfoCreateDialog
from Ui_CreateUser import Ui_Dialog
from Login import db, message

class CreateUserDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(CreateUserDialog, self).__init__(parent)
        self.setupUi(self)
        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        Sno=self.lineEdit.text()
        my_info = StudentInfoCreateDialog(Sno)
        my_info.exec_()
        from StudentInfoCreate import Sflag
        if Sflag==1:
            #学生密码加上掩码'a'
            Spassword=self.lineEdit_3.text()+'a'
            query = QSqlQuery(db)
            sql1="USE [master]"
            sql2="CREATE LOGIN [{0}] WITH PASSWORD=N'{1}', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF".format(Sno, Spassword)
            sql3="USE [Graduate]"
            sql4="CREATE USER [{0}] FOR LOGIN [{0}]".format(Sno)        
            sql5="USE [Graduate]"
            sql6="ALTER ROLE [studentRole] ADD MEMBER [{0}]".format(Sno)
            query.prepare(sql1)
            result1=query.exec_()
            print(result1)
            query.prepare(sql2)
            result2=query.exec_()
            print(result2)
            query.prepare(sql3)
            result3=query.exec_()
            print(result3)
            query.prepare(sql4)
            result4=query.exec_()
            print(result4)
            query.prepare(sql5)
            result5=query.exec_()
            print(result5)
            query.prepare(sql6)
            result6=query.exec_()
            print(result6)
            if (result1)and(result2)and(result3)and(result4)and(result5)and(result6):
                message(u"成功", u"创建学生账号成功，登录名为学号")
            else:
                message(u"失败", u"创建学生账号失败，请不要输入重复的学号")
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        Tno=self.lineEdit_2.text()
        my_info=TeacherInfoCreateDialog(Tno)
        my_info.exec_()
        from TeacherInfoCreate import Tflag
        if Tflag==1:
            #老师密码加上掩码'b'
            Tpassword=self.lineEdit_4.text()+'b'
            query = QSqlQuery(db)
            sql1="USE [master]"
            sql2="CREATE LOGIN [{0}] WITH PASSWORD=N'{1}', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF".format(Tno, Tpassword)
            sql3="USE [Graduate]"
            sql4="CREATE USER [{0}] FOR LOGIN [{0}]".format(Tno)        
            sql5="USE [Graduate]"
            sql6="ALTER ROLE [teacherRole] ADD MEMBER [{0}]".format(Tno)
            query.prepare(sql1)
            result1=query.exec_()
            print(result1)
            query.prepare(sql2)
            result2=query.exec_()
            print(result2)
            query.prepare(sql3)
            result3=query.exec_()
            print(result3)
            query.prepare(sql4)
            result4=query.exec_()
            print(result4)
            query.prepare(sql5)
            result5=query.exec_()
            print(result5)
            query.prepare(sql6)
            result6=query.exec_()
            print(result6)
            if (result1)and(result2)and(result3)and(result4)and(result5)and(result6):
                message(u"成功", u"创建老师账号成功，登录名为工号")
            else:
                message(u"失败", u"创建老师账号失败，请不要输入重复的工号")
