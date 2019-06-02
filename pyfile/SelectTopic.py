# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from Ui_SelectTopic import Ui_Dialog
from PyQt5. QtGui import  *
from PyQt5.QtSql import *
from SelectTopicDialog  import SelectDialog
from Login import db
global model
'''
db = QSqlDatabase.addDatabase('QODBC')
db.setHostName('DESKTOP-8ITEMSI')
db.setDatabaseName('QTDSN')
db.setUserName('csu')
db.setPassword('123')
db.open()
'''

class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        
        query = QSqlQuery(db)
        query.prepare("select TopicNo 课题编号,TopicName 课题名称,Requirement 课题要求,[Population] 选题人数,Teacher.Tno 指导老师工号, Teacher.Tname 指导老师,Teacher.Title 指导老师职称,Teacher.Tphone 指导老师联系方式,School.SchoolName 所在学院 from Topic,Teacher,School where (Topic.Tno=Teacher.Tno)and(Teacher.SchoolNo=School.SchoolNo)")
        print(query.exec())
        self.view(query)


    @pyqtSlot(QModelIndex)
    def on_tableView_pressed(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        # TODO: not implemented yet
        print('table_pressed')
        from Login import role
        if role=="学生":
            selectDialog=SelectDialog(index, model)#传入index和model
            selectDialog.exec_()
        elif role=="教师":
            print('教师只能查看选题')
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        query = QSqlQuery(db)
        query.prepare("select TopicNo 课题编号,TopicName 课题名称,Requirement 课题要求,[Population] 选题人数,Teacher.Tno 指导老师工号, Teacher.Tname 指导老师,Teacher.Title 指导老师职称,Teacher.Tphone 指导老师联系方式,School.SchoolName 所在学院 from Topic,Teacher,School where (Topic.Tno=Teacher.Tno)and(Teacher.SchoolNo=School.SchoolNo)")
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
