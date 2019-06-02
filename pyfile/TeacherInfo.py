# -*- coding: utf-8 -*-

"""
Module implementing TeacherInfoDialog.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5 import *
from Ui_TeacherInfo import Ui_Dialog
from Login import db, message
from PyQt5.QtSql import *

class TeacherInfoDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,account=None,  parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TeacherInfoDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.searchInfo(account)
    
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
    
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_list=[]
        my_list.append('教授')
        my_list.append('副教授')
        my_list.append('讲师')
        my_str,ok=QInputDialog.getItem(self, '职称', '请选择职称', my_list)
        self.lineEdit_6.setText(my_str)
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_str, ok=QInputDialog.getText(self,'出生年月', '在此输入出生年月：19990318',QLineEdit.Normal, '19790318' )
        self.lineEdit_3.setText(my_str)
    
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
        l1=self.lineEdit.text()
        l2=self.lineEdit_2.text()
        l3=self.lineEdit_3.text()
        #判断日期输入格式
        if (re.search(r"(\d{4}-\d{1,2}-\d{1,2})", l3))and((len(l3)>=8)and(len(l3)<=10)):
            print(u"日期输入正确")
        else:
            message(u"错误", u"日期输入错误！请重新输入")
            self.lineEdit_3.setText("")
            l3=""
        l4=self.lineEdit_4.text()
        #判断性别输入格式
        if (re.search(r"男|女",l4))and(len(l4)==1)and(len(l4)==1):
            print(u"性别输入正确")
        else:
            message(u"错误", u"性别输入错误！请重新输入")
            self.lineEdit_4.setText("")
            l4=""
        l5=self.lineEdit_5.text()
        #判断手机号码输入格式
        if (re.search(r"\d{11}", l5))and(len(l5)==11):
            print(u"手机号码输入正确")
        else:
            message(u"错误",u"手机号错误，应为11位数字！请重新输入" )
            self.lineEdit_5.setText("")
            l5=""
        l6=self.lineEdit_6.text()
        #判断班级号输入格式
        if (re.search(r"\S{2,3}", l6))and((len(l6)>=2)and(len(l6)<=3)):
            print(u"职称输入正确")
        else:
            message(u"错误", u"职称输入错误，只能为教授、副教授、讲师其中之一！请重新输入")
            self.lineEdit_6.setText("")
            l6=""
        l7=self.lineEdit_7.text()
        #判断学院号输入格式
        if (re.search(r"\d{2}", l7))and(len(l7)==2):
            print(u"学院号输入正确")
        else:
            message(u"错误",u"学院号错误，应为2位数字！请重新输入" )
            self.lineEdit_7.setText("")
            l7=""
        print("学院号为"+l7)
        #所有数据均输入正确
        if((l1!="")and(l2!="")and(l3!="")and(l4!="")and(l5!="")and(l6!="")and(l7!="")):
            query = QSqlQuery(db)
            query.prepare("\
            update Teacher\
            set Tno='{}',Tname='{}',Tbirth='{}',Tsex='{}',Tphone='{}',Title='{}',SchoolNo='{}'\
            where Tno={}\
            ".format(l1, l2, l3, l4, l5, l6, l7, l1))
            if query.exec():
                message(u"成功",u"数据修改成功" )
            else:
                message1=QMessageBox()
                message1.setText(u"数据修改失败，请输入正确的学院号如左图所示")
                message1.setIconPixmap(QPixmap("School.png"))
                message1.setWindowTitle(u"错误")
                message1.exec_()
    
    def searchInfo(self, account):
        query = QSqlQuery(db)
        query.prepare("select * from Teacher where Tno={}".format(account))
        if query.exec():
            model = QSqlTableModel()
            model.setQuery(query)
            l1=model.index(0,0).data()
            self.lineEdit.setText(l1)
            l2=model.index(0,1).data()
            self.lineEdit_2.setText(l2)
            l3=model.index(0,2).data()
            self.lineEdit_3.setText(l3)
            l4=model.index(0,3).data()
            self.lineEdit_4.setText(l4)
            l5=model.index(0,4).data()
            self.lineEdit_5.setText(l5)
            l6=model.index(0,5).data()
            self.lineEdit_6.setText(l6)
            l7=model.index(0,6).data()
            self.lineEdit_7.setText(str(l7))
        else:
            message(u"错误", u"查询失败")
    
