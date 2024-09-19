from PyQt6.QtWidgets import (QMainWindow,QListWidgetItem,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox,QFileDialog)    
import sys
from main_window import Ui_MainWindow
from PyQt6 import QtCore
import os
class my_ui_mainwindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        """
        Constructor method
        
        Calls the constructor of the base class, then sets up the UI and
        translates it. Finally, it connects the button to the slot method
        show_new_password.
        """
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.actionnew.triggered.connect(self.do_new)
        self.actionsave.triggered.connect(self.do_save)
        self.actionopen.triggered.connect(self.do_open)
        self.actionQuit.triggered.connect(self.do_close)
        self.actionundo.triggered.connect(self.do_undo)
        self.actionredo.triggered.connect(self.do_redo)
        self.actionabout_us.triggered.connect(self.do_about)
    def do_new(self):
        self.notebook.clear()
    def do_save(self):
        filepath,filetype=QFileDialog.getSaveFileName(self,"保存",os.getcwd(),"*.txt")
        if filepath == "":
            return
        with open(filepath,"w",encoding="utf-8") as f:
            f.write(self.notebook.toPlainText())
        QMessageBox.information(self,"提示","保存成功")
    def do_open(self):
        filepath,filetype=QFileDialog.getOpenFileName(self,"打开",os.getcwd(),"*.txt")
        if filepath == "":
            return
        with open(filepath,"r",encoding="utf-8") as f:
            self.notebook.setPlainText(f.read())
        QMessageBox.information(self,"提示","打开成功")
    def do_close(self):
        self.close()
    def do_undo(self):
        self.notebook.undo()
    def do_redo(self):
        self.notebook.redo()
    def do_about(self):
        QMessageBox.about(self,"关于","这是一个简单的记事本")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_mainwindow()
    dialog.show()
    sys.exit(app.exec())
