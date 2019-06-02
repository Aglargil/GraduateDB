# -*- coding: utf-8 -*-

"""
Module implementing StudentInfoListDialog.
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from Ui_SelectTopic import Ui_Dialog
from PyQt5. QtGui import  *
from PyQt5.QtSql import *
from Login import db
global model
from Ui_StudentInfoList import Ui_Dialog
from StudentInfo import Dialog as StudentInfoDialog


class StudentInfoListDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(StudentInfoListDialog, self).__init__(parent)
        self.setupUi(self)
        
        query = QSqlQuery(db)
        query.prepare("select Sno 学号,Sname 姓名,Sbirth 出生日期,Ssex 性别,Sphone 手机号码,Class.ClassName 班级,School.SchoolName 学院,Sgrade 成绩 from Student,Class,School where (Student.ClassNo=Class.ClassNo)and(Student.SchoolNo=School.SchoolNo)and(Class.SchoolNo=School.SchoolNo)")
        print(query.exec())
        self.view(query)
    
    @pyqtSlot(QModelIndex)
    def on_tableView_pressed(self, pindex):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        # TODO: not implemented yet
        from Login import role
        if role=="教师":
            print("教师只能查看学生信息")
        else:
            nowrow=pindex.row()
            account=model.index(nowrow, 0).data()
            my_info=StudentInfoDialog(account)
            my_info.exec_()
            #刷新
            self.on_pushButton_2_clicked()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        query = QSqlQuery(db)
        query.prepare("select Sno 学号,Sname 姓名,Sbirth 出生日期,Ssex 性别,Sphone 手机号码,Class.ClassName 班级,School.SchoolName 学院,Sgrade 成绩 from Student,Class,School where (Student.ClassNo=Class.ClassNo)and(Student.SchoolNo=School.SchoolNo)and(Class.SchoolNo=School.SchoolNo)")
        print(query.exec())
        self.view(query)
    def view(self, query):
        
        global model
        model = QSqlTableModel()
        model.setQuery(query)
        self.tableView.setSelectionBehavior( QtWidgets.QAbstractItemView.SelectRows)#只许选中行
        self.tableView.setSelectionMode (  QtWidgets.QAbstractItemView.SingleSelection)#只许选中单行
        self.tableView.setEditTriggers( QtWidgets.QAbstractItemView.NoEditTriggers)#不允许编辑tableview
                #把数据库显示出来
        self.tableView.setModel(model)
