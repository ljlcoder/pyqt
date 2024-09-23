from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from excel import Ui_Excel
import os,sys,threading,shutil
import pandas as pd
class my_ui_excel(Ui_Excel,QDialog):
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
        self.file_path=""
        self.choose_file.clicked.connect(self.select_file)
        self.choose_dir.clicked.connect(self.output_file)
        self.do_split.clicked.connect(self.split)
    def select_file(self):
        """
        选择文件
        """
        self.file_path=QFileDialog.getOpenFileName(self,'选择文件','./','*.xlsx')[0]
        self.excel_dir.setText(self.file_path)
        df=pd.read_excel(self.file_path)
        cols=list(df.columns)
        self.comboBox.clear()
        self.comboBox.addItems(cols)
    def output_file(self):
        """
        输出目录
        """
        self.output_path=QFileDialog.getExistingDirectory(self,'选择文夹','./')
        self.output_dir.setText(self.output_path)
    def split(self):
        """
        拆分
        """
        df=pd.read_excel(self.file_path)
        col=self.comboBox.currentText()
        df[col].to_excel(os.path.join(self.output_path,"拆分后-"+col+".xlsx"),index=False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_excel()
    dialog.show()
    sys.exit(app.exec())
