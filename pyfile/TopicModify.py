# -*- coding: utf-8 -*-

"""
Module implementing TopicModifyDialog.
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5.QtSql import *
from Login import db
from Ui_TopicModify import Ui_Dialog
from TopicModifyAdd import TopicModifyAddDialog
from TopicModifyMessage import TopicModifyMessageDialog
global model
class TopicModifyDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TopicModifyDialog, self).__init__(parent)
        self.setupUi(self)
        
        query = QSqlQuery(db)
        from Login import account
        from Login import role
        if role=="教师":
            query.prepare("select TopicNo 选题编号,TopicName 选题名称,Requirement 选题要求,[Population] 目前选题人数,Teacher.Tno 指导老师工号,Tname 指导老师姓名 from Topic,Teacher where (Teacher.Tno='{}')and(Topic.Tno=Teacher.Tno)".format(account))
        else:
            query.prepare("select TopicNo 选题编号,TopicName 选题名称,Requirement 选题要求,[Population] 目前选题人数,Teacher.Tno 指导老师工号,Tname 指导老师姓名 from Topic,Teacher where Topic.Tno=Teacher.Tno")
        print(query.exec())
        self.view(query)
    
    @pyqtSlot(QModelIndex)
    def on_tableView_pressed(self, index):
        my_top=TopicModifyMessageDialog(index, model)
        my_top.exec_()
        query = QSqlQuery(db)
        from Login import account
        from Login import role
        if role=="教师":
            query.prepare("select TopicNo 选题编号,TopicName 选题名称,Requirement 选题要求,[Population] 目前选题人数,Teacher.Tno 指导老师工号,Tname 指导老师姓名 from Topic,Teacher where (Teacher.Tno='{}')and(Topic.Tno=Teacher.Tno)".format(account))
        else:
            query.prepare("select TopicNo 选题编号,TopicName 选题名称,Requirement 选题要求,[Population] 目前选题人数,Teacher.Tno 指导老师工号,Tname 指导老师姓名 from Topic,Teacher where Topic.Tno=Teacher.Tno")
        print(query.exec())
        self.view(query)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        # 添加数据后刷新
        my_top=TopicModifyAddDialog()
        my_top.exec_()
        #刷新
        query = QSqlQuery(db)
        from Login import account
        from Login import role
        if role=="教师":
            query.prepare("select TopicNo 选题编号,TopicName 选题名称,Requirement 选题要求,[Population] 目前选题人数,Teacher.Tno 指导老师工号,Tname 指导老师姓名 from Topic,Teacher where (Teacher.Tno='{}')and(Topic.Tno=Teacher.Tno)".format(account))
        else:
            query.prepare("select TopicNo 选题编号,TopicName 选题名称,Requirement 选题要求,[Population] 目前选题人数,Teacher.Tno 指导老师工号,Tname 指导老师姓名 from Topic,Teacher where Topic.Tno=Teacher.Tno")
        print(query.exec())
        self.view(query)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        # 刷新
        query = QSqlQuery(db)
        from Login import account
        from Login import role
        if role=="教师":
            query.prepare("select TopicNo 选题编号,TopicName 选题名称,Requirement 选题要求,[Population] 目前选题人数,Teacher.Tno 指导老师工号,Tname 指导老师姓名 from Topic,Teacher where (Teacher.Tno='{}')and(Topic.Tno=Teacher.Tno)".format(account))
        else:
            query.prepare("select TopicNo 选题编号,TopicName 选题名称,Requirement 选题要求,[Population] 目前选题人数,Teacher.Tno 指导老师工号,Tname 指导老师姓名 from Topic,Teacher where Topic.Tno=Teacher.Tno")
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
