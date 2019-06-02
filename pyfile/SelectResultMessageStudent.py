# -*- coding: utf-8 -*-

"""
Module implementing SelectResultMessageStudentDialog.
"""


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from Login import db, message
global TopicNo
global Tno
global nowrow
from Ui_SelectResultMessageStudent import Ui_Dialog


class SelectResultMessageStudentDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, qindex=None, qmodel=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SelectResultMessageStudentDialog, self).__init__()
        self.setupUi(self)

        index=qindex
        model=qmodel
        global nowrow
        nowrow=index.row()
        global TopicNo
        global Tno
        TopicNo=model.index(nowrow, 0).data()
        Tno=model.index(nowrow, 3).data()
        print('TopicNo='+TopicNo)
        print('Tno='+Tno)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        query=QSqlQuery(db)
        from Login import account
        print("delete from [Select] where(TopicNo='{}')and(Sno='{}')and(Tno='{}')and(Admission='待定')".format(TopicNo, account, Tno))
        query.prepare("delete from [Select] where(TopicNo='{}')and(Sno='{}')and(Tno='{}')and(Admission='待定')".format(TopicNo, account, Tno))
        model = QSqlTableModel()
        model.setQuery(query)
        if query.exec_():
            model.setQuery(query)
            newrow=model.rowCount()
            if newrow<nowrow:
                message(u"成功", u"撤销选题成功")
            else:
                message(u"失败", u"撤销选题失败，您的志愿已被老师同意或拒绝，无法撤销")
