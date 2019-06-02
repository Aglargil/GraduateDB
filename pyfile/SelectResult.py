# -*- coding: utf-8 -*-

"""
Module implementing SelectResultDialog.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import *
from PyQt5.QtSql import *
from SelectResultMessage import SelectResultMessageDialog
from SelectResultMessageStudent import SelectResultMessageStudentDialog
from SelectResultMessageAdmin import SelectResultMessageAdminDialog
from Login import db
from Login import message
from Ui_SelectResult import Ui_Dialog
global model
class SelectResultDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SelectResultDialog, self).__init__(parent)
        self.setupUi(self)
        
        query = QSqlQuery(db)
        from Login import account
        from Login import role
        if role=="学生":
            print("学生只能查看自己的选课结果")
            sql="select Topic.TopicNo 选题编号,Topic.TopicName 选题名称,Topic.Population 当前选题人数,Teacher.Tno 指导老师工号,Teacher.Tname 指导老师,School.SchoolName 老师所在学院,[Select].Wish 志愿,[Select].Admission 录取情况\
                    from [Select],Topic,Teacher,School\
                    where (Teacher.Tno=Topic.Tno)and([Select].TopicNo=Topic.TopicNo)and(School.SchoolNo=Teacher.SchoolNo)and([Select].Tno=Teacher.Tno)and[Select].Sno='{}'".format(account)
        elif role=="教师":
            print("教师可以查看选了自己课题的结果")
            sql="select Student.Sno 学生学号, Student.Sname 学生姓名,Topic.TopicNo 选题编号,Topic.TopicName 选题名称,Topic.Population 当前选题人数,School.SchoolName 学生所在学院,[Select].Wish 志愿,Teacher.Tno 指导老师工号,Teacher.Tname 指导老师,[Select].Admission 录取情况\
                    from [Select],Topic,Teacher,School,Student\
                    where ([Select].TopicNo=Topic.TopicNo)and([Select].Tno=Topic.Tno)and(School.SchoolNo=Student.SchoolNo)and([Select].Tno='{}')and([Select].Tno=Teacher.Tno)and([Select].Sno=Student.Sno)and([Select].Wish='第一志愿')".format(account)
        else:
            print("管理员可以查看选了所有选课结果")
            sql="select Student.Sno 学生学号, Student.Sname 学生姓名,Topic.TopicNo 选题编号,Topic.TopicName 选题名称,Topic.Population 当前选题人数,School.SchoolName 学生所在学院,[Select].Wish 志愿,Teacher.Tno 指导老师工号,Teacher.Tname 指导老师,[Select].Admission 录取情况\
                    from [Select],Topic,Teacher,School,Student\
                    where ([Select].TopicNo=Topic.TopicNo)and([Select].Tno=Topic.Tno)and(School.SchoolNo=Student.SchoolNo)and([Select].Tno=Teacher.Tno)and([Select].Sno=Student.Sno)and([Select].Wish='第一志愿')"
        query=self.queryFunc(sql)
        self.view(query)
    
    @pyqtSlot(QModelIndex)
    def on_tableView_pressed(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        # TODO: not implemented yet
        from Login import role
        from Login import account
        if role=="学生":
            my_mess=SelectResultMessageStudentDialog(index, model)
            my_mess.exec_()
            sql="select Topic.TopicNo 选题编号,Topic.TopicName 选题名称,Topic.Population 当前选题人数,Teacher.Tno 指导老师工号,Teacher.Tname 指导老师,School.SchoolName 老师所在学院,[Select].Wish 志愿,[Select].Admission 录取情况\
                    from [Select],Topic,Teacher,School\
                    where (Teacher.Tno=Topic.Tno)and([Select].TopicNo=Topic.TopicNo)and(School.SchoolNo=Teacher.SchoolNo)and([Select].Tno=Teacher.Tno)and[Select].Sno='{}'".format(account)
            query=self.queryFunc(sql)
        elif role=="教师":
            print("教师可以通过审核")
            my_mess=SelectResultMessageDialog(index, model)
            my_mess.exec_()
            print("教师可以查看选了自己课题的结果")
            sql="select Student.Sno 学生学号, Student.Sname 学生姓名,Topic.TopicNo 选题编号,Topic.TopicName 选题名称,Topic.Population 当前选题人数,School.SchoolName 学生所在学院,[Select].Wish 志愿,Teacher.Tno 指导老师工号,Teacher.Tname 指导老师,[Select].Admission 录取情况\
                    from [Select],Topic,Teacher,School,Student\
                    where ([Select].TopicNo=Topic.TopicNo)and([Select].Tno=Topic.Tno)and(School.SchoolNo=Student.SchoolNo)and([Select].Tno='{}')and([Select].Tno=Teacher.Tno)and([Select].Sno=Student.Sno)and([Select].Wish='第一志愿')".format(account)
            query=self.queryFunc(sql)
        else:
            my_mess=SelectResultMessageAdminDialog(index, model)
            my_mess.exec_()
            sql="select Student.Sno 学生学号, Student.Sname 学生姓名,Topic.TopicNo 选题编号,Topic.TopicName 选题名称,Topic.Population 当前选题人数,School.SchoolName 学生所在学院,[Select].Wish 志愿,Teacher.Tno 指导老师工号,Teacher.Tname 指导老师,[Select].Admission 录取情况\
                    from [Select],Topic,Teacher,School,Student\
                    where ([Select].TopicNo=Topic.TopicNo)and([Select].Tno=Topic.Tno)and(School.SchoolNo=Student.SchoolNo)and([Select].Tno=Teacher.Tno)and([Select].Sno=Student.Sno)and([Select].Wish='第一志愿')"
            query=self.queryFunc(sql)
        self.view(query)
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        from Login import account
        from Login import role
        if role=="学生":
            message(u"错误",u"您不具有审核权限，只有查看权限" )
        elif role=="教师":
            sql="select Student.Sno 学生学号, Student.Sname 学生姓名,Topic.TopicNo 选题编号,Topic.TopicName 选题名称,Topic.Population 当前选题人数,School.SchoolName 学生所在学院,[Select].Wish 志愿,Teacher.Tno 指导老师工号,Teacher.Tname 指导老师,[Select].Admission 录取情况\
                    from [Select],Topic,Teacher,School,Student\
                    where ([Select].TopicNo=Topic.TopicNo)and([Select].Tno=Topic.Tno)and(School.SchoolNo=Student.SchoolNo)and([Select].Tno='{}')and([Select].Tno=Teacher.Tno)and([Select].Sno=Student.Sno)and([Select].Wish='第一志愿')".format(account)
            query=self.queryFunc(sql)
            self.view(query)
            print("第一志愿审核")
        else:
            sql="select Student.Sno 学生学号, Student.Sname 学生姓名,Topic.TopicNo 选题编号,Topic.TopicName 选题名称,Topic.Population 当前选题人数,School.SchoolName 学生所在学院,[Select].Wish 志愿,Teacher.Tno 指导老师工号,Teacher.Tname 指导老师,[Select].Admission 录取情况\
                    from [Select],Topic,Teacher,School,Student\
                    where ([Select].TopicNo=Topic.TopicNo)and([Select].Tno=Topic.Tno)and(School.SchoolNo=Student.SchoolNo)and([Select].Tno=Teacher.Tno)and([Select].Sno=Student.Sno)and([Select].Wish='第一志愿')"
            query=self.queryFunc(sql)
            self.view(query)            
        
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        from Login import account
        from Login import role
        if role=="学生":
            message(u"错误",u"您不具有审核权限，只有查看权限" )
        elif role=="教师":
            #第一志愿被拒绝才会显示第二志愿
            sql="select Student.Sno 学生学号, Student.Sname 学生姓名,Topic.TopicNo 选题编号,Topic.TopicName 选题名称,Topic.Population 当前选题人数,School.SchoolName 学生所在学院,[Select].Wish 志愿,Teacher.Tno 指导老师工号,Teacher.Tname 指导老师,[Select].Admission 录取情况\
                    from [Select],Topic,Teacher,School,Student\
                    where ([Select].TopicNo=Topic.TopicNo)and([Select].Tno=Topic.Tno)and(School.SchoolNo=Student.SchoolNo)and([Select].Tno='{}')and([Select].Tno=Teacher.Tno)and([Select].Sno=Student.Sno)and([Select].Wish='第二志愿')and(Student.Sno in(select Sno from [Select] where (Admission='拒绝')and(Wish='第一志愿')))".format(account)
            query=self.queryFunc(sql)
            self.view(query)
            print("第二志愿审核")
        else:
            sql="select Student.Sno 学生学号, Student.Sname 学生姓名,Topic.TopicNo 选题编号,Topic.TopicName 选题名称,Topic.Population 当前选题人数,School.SchoolName 学生所在学院,[Select].Wish 志愿,Teacher.Tno 指导老师工号,Teacher.Tname 指导老师,[Select].Admission 录取情况\
                    from [Select],Topic,Teacher,School,Student\
                    where ([Select].TopicNo=Topic.TopicNo)and([Select].Tno=Topic.Tno)and(School.SchoolNo=Student.SchoolNo)and([Select].Tno=Teacher.Tno)and([Select].Sno=Student.Sno)and([Select].Wish='第二志愿')and(Student.Sno in(select Sno from [Select] where (Admission='拒绝')and(Wish='第一志愿')))"
            query=self.queryFunc(sql)
            self.view(query)
            print("第二志愿审核")
            
    def view(self, query):
        global model
        model = QSqlTableModel()
        model.setQuery(query)
        self.tableView.setSelectionBehavior( QtWidgets.QAbstractItemView.SelectRows)#只许选中行
        self.tableView.setSelectionMode (  QtWidgets.QAbstractItemView.SingleSelection)#只许选中单行
        self.tableView.setEditTriggers( QtWidgets.QAbstractItemView.NoEditTriggers)#不允许编辑tableview
                        #把数据库显示出来
        self.tableView.setModel(model)
    
    def queryFunc(self, sql):
        query = QSqlQuery(db)
        print(query.exec(sql))
        return query
