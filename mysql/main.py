from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QTableWidgetItem,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
from login import Ui_Login
from schedule_main import my_ui_schedule
import sys
from demo import DB
class my_ui_excel(Ui_Login,QDialog):
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
        self.pushButton_login.clicked.connect(self.login)
    def login(self):
        self.username=self.lineEdit_username.text()
        self.password=self.lineEdit_password.text()
        if self.username=="" or self.password=="":
            QMessageBox.warning(self, "警告", "用户名或密码不能为空!", QMessageBox.Ok)
            return
        sql=f"""
            select count(1) from users where user_name='{self.username}' and user_pwd='{self.password}';
        """
        db = DB()
        conn=db.get_conn()
        res=db.query_sql(conn,sql)
        print(res[0][0])
        if len(res)==((1,),):
            row=res[0]
            user_id=row["user_id"]
            user_name=row["user_name"]
            QMessageBox.information(self, "提示", "登录成功!")
            window=my_ui_schedule(conn=conn,userid=user_id,username=user_name)
            if window.exec() == QDialog.DialogCode.Accepted:
                QMessageBox.information(self, "提示", "登录成功!")
            db.close_conn(conn)
        else:
            QMessageBox.warning(self, "警告", "用户名或密码错误!")
            db.close_conn(conn)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_excel()
    dialog.show()
    sys.exit(app.exec())
