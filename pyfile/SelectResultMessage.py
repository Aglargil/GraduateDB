# -*- coding: utf-8 -*-

"""
Module implementing SelectResultMessageDialog.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from Login import db
from Ui_SelectResultMessage import Ui_Dialog
global TopicNo
global Sno
global Tno

class SelectResultMessageDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,qindex=None,  qmodel=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SelectResultMessageDialog, self).__init__()
        self.setupUi(self)
        
        index=qindex
        model=qmodel
        nowrow=index.row()
        global TopicNo
        global Sno
        global Tno
        TopicNo=model.index(nowrow, 2).data()
        Sno=model.index(nowrow, 0).data()
        Tno=model.index(nowrow, 7).data()
        print('TopicNo='+TopicNo)
        print('Sno='+Sno)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        query = QSqlQuery(db)
                #判断该学生是否有一个志愿被通过
        query.prepare("select * from [Select] where Sno='{}'".format(Sno))
        query.exec_()
        model = QSqlTableModel()
        model.setQuery(query)
        try:
            ad1=model.index(0, 4).data()
            print("try ad1="+ad1)
        except:
            ad1="拒绝"
        try:
            ad2=model.index(1, 4).data()
            print("try ad2="+ad2)
        except:
            ad2="拒绝"
        if(((ad1=="拒绝")or((ad1=="待定")))and((ad2=="拒绝")or(ad2=="待定"))):
            print("update [Select] set Admission='同意' where Sno='{}'and TopicNo='{}' and Tno='{}'".format(Sno, TopicNo, Tno))
            query.prepare("update [Select] set Admission='同意' where Sno='{}'and TopicNo='{}' and Tno='{}'".format(Sno, TopicNo, Tno))
            query.exec_()
            message=QMessageBox()
            message.setText(u"该学生已通过审核")
            message.setWindowTitle(u"成功！")
            message.exec_()
        else:
            message=QMessageBox()
            message.setText(u"该学生已经有一个志愿通过审核，无法再次通过")
            message.setWindowTitle(u"错误")
            message.exec_()
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        query = QSqlQuery(db)
        #判断该学生是否有一个志愿被通过
        query.prepare("select * from [Select] where Sno='{}'".format(Sno))
        query.exec_()
        model = QSqlTableModel()
        model.setQuery(query)
        try:
            ad1=model.index(0, 4).data()
            print("try ad1="+ad1)
        except:
            ad1="拒绝"
        try:
            ad2=model.index(1, 4).data()
            print("try ad2="+ad2)
        except:
            ad2="拒绝"
        if((ad1=="拒绝")and(ad2=="拒绝")):
            message=QMessageBox()
            message.setText(u"该学生的该志愿已经被拒绝")
            message.setWindowTitle(u"错误")
            message.exec_()
        else:
            print("update [Select] set Admission='拒绝' where Sno='{}'and TopicNo='{}' and Tno='{}'".format(Sno, TopicNo, Tno))
            query.prepare("update [Select] set Admission='拒绝' where Sno='{}'and TopicNo='{}' and Tno='{}'".format(Sno, TopicNo, Tno))
            query.exec_()
            message=QMessageBox()
            message.setText(u"该学生未通过审核")
            message.setWindowTitle(u"成功")
            message.exec_()
