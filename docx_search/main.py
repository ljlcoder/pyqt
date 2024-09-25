from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from docx_search import Ui_Search
import os,sys,threading,shutil
import pandas as pd
from demo import File_reader
class my_ui_excel(Ui_Search,QDialog):
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
        self.choose.clicked.connect(self.choose_dir)
        self.search.clicked.connect(self.search_words)
        self.open.clicked.connect(self.open_dir)
    def choose_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        self.lineEdit_dir.setText(dir_path)
    def search_words(self):
        if self.lineEdit_search.text() == "":
            QMessageBox.information(self, "提示", "请输入要搜索的关键词")
            return
        search_words = self.lineEdit_search.text()
        search_words=search_words.strip()
        self.listWidget.clear()
        for root, dirs, files in os.walk(self.lineEdit_dir.text()):
            for file in files:
                file_path = os.path.join(root, file)
                if file.startswith("~$"):
                    continue
                if file.endswith(".docx"):
                    File_reader().read_docx(file_path)
                elif file.endswith(".txt"):
                    File_reader().read_txt(file_path)
                elif file.endswith(".xlsx"):
                    File_reader().read_excel(file_path)
                elif file.endswith(".pptx"):
                    File_reader().read_pptx(file_path)
                if search_words in file_path.split("\\")[-1]:
                    item = QListWidgetItem(file_path)
                    self.listWidget.addItem(item)
        QMessageBox.information(self, "提示", "搜索完成")
    def open_dir(self):
        if self.listWidget.currentItem() == None:
            QMessageBox.information(self, "提示", "请选择要打开的文件")
            return
        os.startfile(self.listWidget.currentItem().text())
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_excel()
    dialog.show()
    sys.exit(app.exec())
