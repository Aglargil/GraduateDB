# -*- coding: utf-8 -*-

"""
Module implementing SelectTopicDialog.
"""

from PyQt5.QtCore import pyqtSlot,  QModelIndex
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from Ui_SelectTopicDialog import Ui_Dialog
from Login import db
from Login import message
#传入index和model
class SelectDialog(QDialog, Ui_Dialog, QModelIndex, QSqlTableModel):
    """
    Class documentation goes here.
    """
    
    def __init__(self,  qindex=None, qmodel=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SelectDialog, self).__init__()
        self.setupUi(self)
        
        model=qmodel
        nowrow=qindex.row()
        global TopicNo
        global Tno
        TopicNo=model.index(nowrow, 0).data()
        Tno=model.index(nowrow, 4).data()
        print('TopicNo='+TopicNo)
        print('Tno='+Tno)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("select_topic")
        #判断当前是否已经选择了课题，若一个课题都没选择，则为第一志愿
        query = QSqlQuery(db)
        from Login import account
        query.prepare("select * from [Select] where Sno='{}'".format(account))
        query.exec_()
        model = QSqlTableModel()
        model.setQuery(query)
        nowrow=model.rowCount()
        print("nowrow="+str(nowrow))
        if(nowrow==0):
            query.prepare("insert into [Select](TopicNo,Sno,Tno,Wish,Admission) values('{}','{}','{}','第一志愿','待定')".format(TopicNo, account, Tno))
            if(query.exec_()):
                message(u"成功",u"选取第一志愿成功！" )
        elif(nowrow==1):
            query.prepare("insert into [Select](TopicNo,Sno,Tno,Wish,Admission) values('{}','{}','{}','第二志愿','待定')".format(TopicNo, account, Tno))
            if(query.exec_()):
                message(u"成功",u"选取第二志愿成功！" )
            else:
                message(u"失败",u"您已经选择该志愿作为第一志愿")
        else:
            message(u"警告", u"您已经选择了两个志愿！请取消志愿后再选取")
