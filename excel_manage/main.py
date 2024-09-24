from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox,QTableWidgetItem)    
import sys
from manage import Ui_manage
import os,sys,threading,shutil
import pandas as pd
from add_main import my_ui_add
from show_main import my_ui_static
class my_ui_excel(Ui_manage,QDialog):
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
        self.pushButton.clicked.connect(self.select_file)
        self.pushButton_select.clicked.connect(self.Search)
        self.add_single_data.clicked.connect(self.add_single)
        self.remove_data.clicked.connect(self.remove)
        self.change_data.clicked.connect(self.change)
        self.pushButton_show.clicked.connect(self.statics)
    def show_df_in_table(self,data):
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data.columns))
        for i in range(len(data)):
            for j in range(len(data.columns)):
                item=QTableWidgetItem(str(data.iloc[i,j]))
                self.tableWidget.setItem(i,j,item)
    def add_single(self):
        """
        添加单条数据
        """
        window=my_ui_add(self.file_path)
        if window.exec() == QDialog.DialogCode.Accepted:
            df=pd.read_excel(self.file_path)
            self.show_df_in_table(df)
            QMessageBox.information(self,"提示","添加成功")
    def remove(self):
        """
        删除数据
        """
        if self.tableWidget.currentRow()==-1:
            QMessageBox.critical(self,"错误","请选择要删除的数据")
            return
        df=pd.read_excel(self.file_path)
        df=df.drop(self.tableWidget.currentRow())
        df.to_excel(self.file_path,index=False)
        self.show_df_in_table(df)
        QMessageBox.information(self,"提示","删除成功")
    def change(self):
        """
        修改数据
        """
        if self.tableWidget.currentRow()==-1:
            QMessageBox.critical(self,"错误","请选择要修改的数据")
            return
        window=my_ui_add(self.file_path)#,self.tableWidget.currentRow())
        if window.exec() == QDialog.DialogCode.Accepted:
            df=pd.read_excel(self.file_path)
            self.show_df_in_table(df)
            QMessageBox.information(self,"提示","修改成功")
    def statics(self):
        """
        统计数据
        """
        window=my_ui_static(data=self.file_path)
        if window.exec() == QDialog.DialogCode.Accepted:

            df=pd.read_excel(self.file_path)
            data={
                "语文":{
                    "最高分":round(df["语文"].max(),2),
                    "最低分":round(df["语文"].min(),2),
                    "平均分":round(df["语文"].mean(),2),
                },
                "数学":{   
                    "最高分":round(df["数学"].max(),2),
                    "最低分":round(df["数学"].min(),2),
                    "平均分":round(df["数学"].mean(),2),
                }
            }
            # self.show_df_in_table(df)
            QMessageBox.information(self,"提示","统计成功")

    def select_file(self):
        """
        选择文件
        """
        self.file_path,ok=QFileDialog.getOpenFileName(self,"选择文件",os.getcwd(),"All Files (*);;Text Files (*.txt)")
        if ok:
            self.label_excel.setText(self.file_path)
            df=pd.read_excel(self.file_path)
            self.show_df_in_table(df)
        QMessageBox.information(self,"提示","文件读取成功")
    
    def Search(self):
        """
        搜索
        """
        if self.lineEdit.text()=="":
            QMessageBox.critical(self,"错误","请输入搜索内容")
            return
        keyword=self.lineEdit.text()
        if keyword:
            df=pd.read_excel(self.file_path)
            df=df[(df["学号"]==keyword) | (df["姓名"]==keyword)]
            self.show_df_in_table(df)
        else:
            df=pd.read_excel(self.file_path)
            self.show_df_in_table(df)
        QMessageBox.information(self,"提示","搜索成功")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_excel()
    dialog.show()
    sys.exit(app.exec())


#TypeError: setItem(self, row: int, column: int, item: QTableWidgetItem): argument 3 has unexpected type 'QListWidgetItem'  
#<PyQt6.QtWidgets.QLineEdit object at 0x000002703CDBD480>