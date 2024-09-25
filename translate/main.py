from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QTableWidgetItem,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
import os,sys,threading,shutil
import pandas as pd
import pickle
from translate import Ui_translate
from get_agg_res import get_agg_res
class my_ui_excel(Ui_translate,QDialog):
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
        self.eng_list=self.load_dict()
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_jieba.clicked.connect(self.jieba)
        self.pushButton_m_search.clicked.connect(self.m_search)
    def load_dict(self):
        fapth="H:\python\pyqt\\translate\\text.txt"
        if not os.path.exists(fapth):
            QMessageBox.critical(self,"错误","没有找到文件")
            self.close()
        with open(fapth,"rb") as f:
            return pickle.load(f)
    def search(self):
        eng=self.lineEdit.text()
        if eng == "":
            QMessageBox.critical(self,"错误","没有输入单词")
            return
        tranlate=self.load_dict.get(eng,None)
        tranlate=str(tranlate).replace("\\n","\n")
        self.plainTextEdit.setText(tranlate)
        QMessageBox.critical(self,"错误","没有找到该单词")
    def jieba(self):
        text=self.plainTextEdit.toPlainText()
        if text == "":
            QMessageBox.critical(self,"错误","没有输入单词")
            return
        df_agg=get_agg_res(text)
        self.tableWidget.setRowCount(len(df_agg))
        self.tableWidget.setColumnCount(2)
        for i in range(len(df_agg)):
            for j in range(2):
                item=QTableWidgetItem(str(df_agg.index[i]))
                self.tableWidget.setItem(i,j,item)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_excel()
    dialog.show()
    sys.exit(app.exec())
