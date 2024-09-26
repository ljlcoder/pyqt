from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QTableWidgetItem,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
from schedule import Ui_schedule
from content_main import my_ui_content
import sys
import pandas as pd
class my_ui_schedule(Ui_schedule,QDialog):
    def __init__(self,conn,userid,username):
        """
        Constructor method
        
        Calls the constructor of the base class, then sets up the UI and
        translates it. Finally, it connects the button to the slot method
        show_new_password.
        """
        super().__init__()
        self.setupUi(self)  
        self.conn=conn
        self.userid=userid
        self.username=username
        self.retranslateUi(self)
        self.show_data()
        self.pushButton_export.clicked.connect(self.export)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_commit.clicked.connect(self.commit)
    def add(self):
        window=my_ui_content(conn=self.conn,userid=self.userid,username=self.username)
        if window.exec() == QDialog.DialogCode.Accepted:
            self.show_data()
            QMessageBox.information(self,"提示","添加成功")
        else:
            QMessageBox.information(self,"提示","添加失败")

    def export(self):
        sql=f"select * from schedule where user_id={self.userid};"
        df=pd.read_sql(sql,self.conn)
        filepath, ok = QFileDialog.getSaveFileName(self, "保存文件", "", "CSV Files (*.csv)")
        df.to_csv(filepath,encoding="gbk",index=False)
    def 
    def show_data(self):    
        sql=f"select * from schedule where user_id={self.userid};"
        rows=self.conn.query_sql(sql)
        #self.tableWidget.clear()
        self.tableWidget.setRowCount(len(rows))
        row_num=0
        for row in rows:
            self.tableWidget.setItem(row_num,0,QTableWidgetItem(str(row["schedule_id"])))
            self.tableWidget.setItem(row_num,1,QTableWidgetItem(str(row["schedule_name"])))
            self.tableWidget.setItem(row_num,2,QTableWidgetItem(str(row["schedule_date"])))
            self.tableWidget.setItem(row_num,3,QTableWidgetItem(str(row["schedule_time"])))
            self.tableWidget.setItem(row_num,4,QTableWidgetItem(str(row["schedule_content"])))
            row_num+=1
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_schedule()
    dialog.show()
    sys.exit(app.exec())
