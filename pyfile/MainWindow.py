# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5 import *
from Ui_MainWindow import Ui_MainWindow
from StudentInfo import Dialog as StudentInfoDialog
from SelectTopic import Dialog as SelectTopicDialog
from Login import LoginDialog, flag
from TeacherInfo import TeacherInfoDialog
from StudentInfoList import StudentInfoListDialog
from TeacherInfoList import TeacherInfoListDialog
from SelectResult import SelectResultDialog
from TopicModify import TopicModifyDialog
from Login import message
from CreateUser import CreateUserDialog
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Treetog-I-Documents.ico"))
        self.setWindowIcon(icon)
        my_login=LoginDialog()
        my_login.exec_()
        from Login import  flag
        global flag
        print("flag="+str(flag))
        
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        from Login import role
        if role=="管理员":
            my_create=CreateUserDialog()
            my_create.exec_()
        else:
            message(u"错误", u"您不具有该权限")
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        from Login import role
        from Login import account
        if role=="学生":
            my_info=StudentInfoDialog(account)
        else:
            my_info=StudentInfoListDialog()
        my_info.exec_()
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_info=SelectTopicDialog()
        my_info.exec_()
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        from Login import role
        from Login import account
        if role=="教师":
            my_info=TeacherInfoDialog(account)
        else:
            my_info=TeacherInfoListDialog()
        my_info.exec_()

    
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        my_info=SelectResultDialog()
        my_info.exec_()
    
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        from Login import role
        if role=="学生":
            message(u"错误", u"您不具有修改选题的权限")
        else:
            my_top = TopicModifyDialog()
            my_top.exec_()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    #成功登录才显示主界面
    print(flag)
    if(flag==1):
        ui.show()
    sys.exit(app.exec_())
