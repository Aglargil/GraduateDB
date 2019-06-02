# -*- coding: utf-8 -*-

"""
Module implementing TopicModifyAddDialog.
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5.QtSql import *
from Login import db
from Login import message
from Ui_TopicModifyAdd import Ui_Dialog


class TopicModifyAddDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TopicModifyAddDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.lineEdit_4.setPlaceholderText('教师不允许修改教师编号')
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        l1=self.lineEdit.text()
        l2=self.lineEdit_2.text()
        l3=self.lineEdit_3.text()
        from Login import role
        query = QSqlQuery(db)
        if role=="教师":
            from Login import account
            query.prepare("insert into Topic values('{}','{}','{}','0','{}')".format(l1, l2, l3, account))
            if query.exec():
                message(u"成功", u"数据添加成功")
            else:
                message(u"错误", u"数据添加失败，请不要插入带重复编号的选题")
                self.lineEdit.setText('')
        else:
            l4=self.lineEdit_4.text()
            query.prepare("insert into Topic values('{}','{}','{}','0','{}')".format(l1, l2, l3, l4))
            if query.exec():
                message(u"成功", u"数据添加成功")
            else:
                message(u"错误", u"数据添加失败，该工号的老师不存在或该工号的老师已经有该编号的选题")
                self.lineEdit.setText('')   
                self.lineEdit_4.setText('')   
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        #清除
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
