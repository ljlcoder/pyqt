from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox,QTableWidgetItem)    
import sys
from show import Ui_static_2
import os,sys,threading,shutil
import pandas as pd
class my_ui_static(Ui_static_2,QDialog):
    def __init__(self,data):
        """
        Constructor method
        
        Calls the constructor of the base class, then sets up the UI and
        translates it. Finally, it connects the button to the slot method
        show_new_password.
        """
        super().__init__()
        self.setupUi(self)  
        self.retranslateUi(self)
        row_config={
            "语文":0,
            "数学":1,
            "英语":2
        }
        col_config={
            "最高分":0,
            "最低分":1,
            "平均分":2
        }
        for course in data:
            row=row_config[course]
            for col in data[course]:
                col=col_config[col]
                item=QTableWidgetItem(str(data[course][col]))
                self.tableWidget.setItem(row,col,item)
        self.accept()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_static()
    dialog.show()
    sys.exit(app.exec())


#TypeError: setItem(self, row: int, column: int, item: QTableWidgetItem): argument 3 has unexpected type 'QListWidgetItem'  