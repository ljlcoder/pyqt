from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from concat import Ui_Dialog
import os,sys,threading,shutil
import pandas as pd
# import excel_utils
class my_ui_excel(Ui_Dialog,QDialog):
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
        self.choose_dir.clicked.connect(self.select_dir)
        self.rm_file.clicked.connect(self.remove_file)
        self.save.clicked.connect(self.save_file)
    def select_dir(self):
        """
        选择文件
        """
        path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
        self.lineEdit.setText(path)
        self.listWidget.clear()
        for fname in os.listdir(path):
            if fname.endswith(".xlsx"):
                self.listWidget.addItem(fname)
    def remove_file(self):
        """
        删除文件
        """
        item = self.listWidget.currentItem()
        if item == "":
            QMessageBox.critical(self,"错误","请先选择文件")
            return
        path = os.path.join(self.lineEdit.text(),item.text())
        os.remove(path)
        self.listWidget.takeItem(self.listWidget.row(item))
        QMessageBox.information(self,"提示","删除成功")
    def save_file(self):
        """
        保存文件
        """
        if self.lineEdit.text() == "":
            QMessageBox.critical(self,"错误","请先选择文件夹")
            return
        filepath = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
        df_lists=[]
        for i in range(self.listWidget.count()):
            item=self.listWidget.item(i)
            df_lists.append(item.text())
        pd.concat(df_lists).to_excel(filepath+"/拼接后.xlsx",index=False)
        #pd.concat([pd.read_excel(os.path.join(self.lineEdit.text(),i)) for i in self.listWidget.selectedItems()]).to_excel(filepath+"/拼接后.xlsx")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_excel()
    dialog.show()
    sys.exit(app.exec())


# pip install XXX -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com 