# -*- coding: utf-8 -*-

"""
Module implementing TopicModifyMessageDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from Login import db
from Ui_TopicModifyMessage import Ui_Dialog
from TopicModifyMessageModify import TopicModifyMessageModifyDialog
class TopicModifyMessageDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, pindex=None, pmodel=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TopicModifyMessageDialog, self).__init__()
        self.setupUi(self)
        
        nowrow=pindex.row()
        global TopicNo
        TopicNo=pmodel.index(nowrow, 0).data()
        global Tno
        Tno=pmodel.index(nowrow, 4).data()
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # 传入TopicNo,Tno
        my_top=TopicModifyMessageModifyDialog(TopicNo, Tno)
        my_top.exec_()
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        #删除数据
        query = QSqlQuery(db)
        query.prepare("delete from Topic where (TopicNo='{}')and(Tno='{}')".format(TopicNo, Tno))
        if(query.exec_()):
            message=QMessageBox()
            message.setText(u"删除数据成功")
            message.setWindowTitle(u"成功")
            message.exec_()
        else:
            message=QMessageBox()
            message.setText(u"删除数据失败")
            message.setWindowTitle(u"错误")
            message.exec_()
