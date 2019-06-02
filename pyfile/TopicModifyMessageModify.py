# -*- coding: utf-8 -*-

"""
Module implementing TopicModifyMessageModifyDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from Login import db
from Ui_TopicModifyMessageModify import Ui_Dialog


class TopicModifyMessageModifyDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, pTopicNo=None, pTno=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TopicModifyMessageModifyDialog, self).__init__()
        self.setupUi(self)
        
        query = QSqlQuery(db)
        from Login import role
        #如果是管理员，可修改编号
        if role=="管理员":
            self.lineEdit_3.setReadOnly(False)
        global TopicNo
        TopicNo=pTopicNo
        global Tno
        Tno=pTno
        query.prepare("select * from Topic where (TopicNo='{}')and(Tno='{}')".format(TopicNo, Tno))
        query.exec_()
        model = QSqlTableModel()
        model.setQuery(query)
        l1=model.index(0, 1).data()
        l2=model.index(0, 2).data()
        global account
        account=model.index(0, 4).data()
        self.lineEdit.setText(l1)
        self.lineEdit_2.setText(l2)
        self.lineEdit_3.setText(account)    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        l1=self.lineEdit.text()
        l2=self.lineEdit_2.text()
        l3=self.lineEdit_3.text()
        print("update Topic set TopicName='{}',Requirement='{}',Tno='{}' where (TopicNo='{}')and(Tno='{}')".format(l1, l2,l3, TopicNo, account))
        query = QSqlQuery(db)
        query.prepare("update Topic set TopicName='{}',Requirement='{}',Tno='{}' where (TopicNo='{}')and(Tno='{}')".format(l1, l2,l3,  TopicNo, account))
        if(query.exec_()):
            message=QMessageBox()
            message.setText(u"修改数据成功")
            message.setWindowTitle(u"成功")
            message.exec_()
        else:
            message=QMessageBox()
            message.setText(u"修改数据失败,此老师不存在,或此老师已经有编号为"+TopicNo+u"的数据")
            message.setWindowTitle(u"错误")
            message.exec_()
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
