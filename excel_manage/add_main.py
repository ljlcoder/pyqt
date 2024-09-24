from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox,QTableWidgetItem)    
import sys
from add import Ui_add
import os,sys,threading,shutil
import pandas as pd
class my_ui_add(Ui_add,QDialog):
    def __init__(self,file_path):
        """
        Constructor method
        
        Calls the constructor of the base class, then sets up the UI and
        translates it. Finally, it connects the button to the slot method
        show_new_password.
        """
        super().__init__()
        self.setupUi(self)  
        self.retranslateUi(self)
        self.file_path=file_path
        self.submmit.clicked.connect(self.add)
    def add(self):
        if self.sno.text() == "" or self.name.text() == "" or self.chinese.text() == "" or self.English.text() == "" or self.math.text() == "":
            QMessageBox.critical(self, "错误", "请输入完整信息")
            return
        df=pd.read_excel(self.file_path)
        df_new=pd.DataFrame({
            "学号":[self.sno.text()],
            "姓名":[self.name.text()],
            "语文":[self.chinese.text()],
            "数学":[self.math.text()],
            "英语":[self.English.text()]
        })
        df=pd.concat([df,df_new]).to_excel(self.file_path,index=False) 
        QMessageBox.information(self, "提示", "添加成功")
        self.accept()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_add()
    dialog.show()
    sys.exit(app.exec())


#TypeError: setItem(self, row: int, column: int, item: QTableWidgetItem): argument 3 has unexpected type 'QListWidgetItem'  