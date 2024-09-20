from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from rm_dir import Ui_rm_dir
import os,sys,threading,shutil
class my_ui_stock(Ui_rm_dir,QDialog):
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
        self.filedir_path=""
        self.pushButton_dir.clicked.connect(self.select_dir)
        self.pushButton_remove.clicked.connect(self.rm_dir)
        self.pushButton_scan.clicked.connect(self.scan_dir)
    def select_dir(self):
        self.filedir_path=QFileDialog.getExistingDirectory(self,"选择文件夹",os.getcwd())
        if self.filedir_path=="":
            return
        self.lineEdit_dir.setText(self.filedir_path)
    def scan_dir(self):
        if self.lineEdit_dir.text()=="":
            QMessageBox.critical(self,"错误","请先选择文件夹")
            return
        #递归扫描文件夹
        file_list=[]
        for root,dirs,files in os.walk(self.lineEdit_dir.text()):
            for file in files:
                file_path=os.path.join(root,file)
                file_size=round(os.path.getsize(file_path)/1024/1024,4)
                file_list.append((file_path,file_size))
        self.listWidget.clear()
        file_list.sort(key=lambda x:x[1],reverse=True)
        for file_path,file_size in file_list:
            item=QListWidgetItem()
            item.setText(f"{file_path} {file_size}MB")
            self.listWidget.addItem(item)
                #self.listWidget.addItem(os.path.join(root,file),os.path.getsize(os.path.join(root,file))/1024/1024)
        QMessageBox.information(self,"提示","扫描完成")
    def rm_dir(self):
        item=self.listWidget.currentItem()
        if item=="":
            QMessageBox.critical(self,"错误","请先扫描文件夹")
            return
        filepath=str(item.text())[:str(item.text()).rfind(" ")]
        if os.path.isfile(filepath):
            os.remove(filepath)
        self.listWidget.takeItem(self.listWidget.row(item))
        QMessageBox.information(self,"提示","删除成功")
        #self.listWidget.clear()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_stock()
    dialog.show()
    sys.exit(app.exec())
