# -*- coding: utf-8 -*-

"""
Module implementing TeacherInfoListDialog.
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
from Ui_TeacherInfoList import Ui_Dialog
from TeacherInfo import  TeacherInfoDialog


class TeacherInfoListDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TeacherInfoListDialog, self).__init__(parent)
        self.setupUi(self)
        
        query = QSqlQuery(db)
        query.prepare("select Tno 工号,Tname 姓名,Tbirth 出生日期,Tsex 性别,Tphone 手机号码,Title 职称,School.SchoolName 学院 from Teacher,School where (Teacher.SchoolNo=School.SchoolNo)")
        print(query.exec())
        self.view(query)
    
    @pyqtSlot(QModelIndex)
    def on_tableView_pressed(self, pindex):
        #刷新
        from Login import role
        if role =="学生":
            print("学生只能查看数据")
        else:
            nowrow=pindex.row()
            account=model.index(nowrow, 0).data()
            my_info=TeacherInfoDialog(account)
            my_info.exec_()
            self.on_pushButton_2_clicked()
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        query = QSqlQuery(db)
        query.prepare("select Tno 工号,Tname 姓名,Tbirth 出生日期,Tsex 性别,Tphone 手机号码,Title 职称,School.SchoolName 学院 from Teacher,School where (Teacher.SchoolNo=School.SchoolNo)")
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
