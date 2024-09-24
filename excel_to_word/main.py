from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from e_to_w import Ui_e_to_w
import os,sys,threading,shutil
import pandas as pd
from docxtpl import DocxTemplate
from datetime import datetime
class my_ui_e_to_w(Ui_e_to_w,QDialog):
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
        # self.excel.path=""
        # self.word.path=""
        # self.dir.path=""
        self.pushButton.clicked.connect(self.do_choose_excel)
        self.pushButton_2.clicked.connect(self.do_choose_word)
        self.pushButton_3.clicked.connect(self.do_choose_dir)
        self.pushButton_4.clicked.connect(self.do_generate_words)

    def do_choose_excel(self):
        self.file_path = QFileDialog.getOpenFileName(self, "选择要转换的Excel文件", "", "Excel Files (*.xlsx *.xls)")[0]
        self.lineEdit.setText(self.file_path)
        QMessageBox.information(self, "提示", "文件读取成功")
    def do_choose_word(self):
        self.file_path = QFileDialog.getOpenFileName(self, "选择要保存的Word文件", "", "Word Files (*.docx)")[0]
        self.lineEdit_2.setText(self.file_path)
        QMessageBox.information(self, "提示", "文件读取成功")

    def do_choose_dir(self):
        self.file_path = QFileDialog.getExistingDirectory(self, "选择要保存的目录") 
        self.lineEdit_3.setText(self.file_path)
        QMessageBox.information(self, "提示", "文件读取成功")

    def do_generate_words(self):
        # if self.lineEdit == "" or self.lineEdit_2 == "" or self.lineEdit_3 == "":
        #     QMessageBox.critical(self, "错误", "请输入完整信息")
        #     return
        df = pd.read_excel(self.lineEdit.text())
        doc=DocxTemplate(self.lineEdit_2.text())
        cur_date=datetime.now().strftime("%Y-%m-%d")
        for idx,row in df.iterrows():
            data={
                "姓名":row["姓名"],
                "语文":row["语文"],
                "数学":row["数学"],
                "英语":row["英语"],
                "总分":round(float(row["语文"])+float(row["数学"])+float(row["英语"]),2),
                "时间":cur_date
            }
            doc.render(data)
            doc.save(self.lineEdit_3.text() + "/" + row["姓名"] + ".docx")
        QMessageBox.information(self, "提示", "文件生成成功")
        os.startfile(self.lineEdit_3.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_e_to_w()
    dialog.show()
    sys.exit(app.exec())

# pip install XXX -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com