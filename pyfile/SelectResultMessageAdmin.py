# -*- coding: utf-8 -*-

"""
Module implementing SelectResultMessageDialog.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from Login import db, message
from Ui_SelectResultMessageAdmin import Ui_Dialog
global TopicNo
global Sno
global Tno

class SelectResultMessageAdminDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,qindex=None,  qmodel=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SelectResultMessageAdminDialog, self).__init__()
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
            message(u"成功！", u"该学生已通过审核")
        else:
            message(u"错误", u"该学生已经有一个志愿通过审核，无法再次通过")
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
            message(u"错误",u"该学生的该志愿已经被拒绝" )
        else:
            print("update [Select] set Admission='拒绝' where Sno='{}'and TopicNo='{}' and Tno='{}'".format(Sno, TopicNo, Tno))
            query.prepare("update [Select] set Admission='拒绝' where Sno='{}'and TopicNo='{}' and Tno='{}'".format(Sno, TopicNo, Tno))
            query.exec_()
            message(u"成功", u"该学生未通过审核")
            
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        query=QSqlQuery(db)
        print("delete from [Select] where(TopicNo='{}')and(Sno='{}')and(Tno='{}')".format(TopicNo, Sno, Tno))
        query.prepare("delete from [Select] where(TopicNo='{}')and(Sno='{}')and(Tno='{}')".format(TopicNo, Sno, Tno))
        query.exec_()
        model = QSqlTableModel()
        model.setQuery(query)
        oldrow=model.rowCount()
        if query.exec_():
            model.setQuery(query)
            newrow=model.rowCount()
            if newrow<oldrow:
                message(u"成功", u"撤销选题成功")
            else:
                message(u"失败", u"撤销选题失败，您的志愿已被老师同意或拒绝，无法撤销")
