from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from code import Ui_codegenerate as codegenerate
import string
import random
class mycodegenerate(codegenerate,QDialog):
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
        self.pushButton.clicked.connect(self.show_new_password)

    def show_new_password(self): 
        """
        Slot method to generate a new password.
        
        This method is connected to the button clicked signal and generates a
        new password with 20 random characters from a string containing
        letters, digits and punctuation. The generated password is then set as
        the text of the line edit widget. Finally, a message box pops up with
        the message " " (Password generated successfully).
        """
        site=self.lineEdit_site.text()
        if not site:
            QMessageBox.warning(self,"警告","请输入网站名称")
            return
        words=[]
        if self.checkBox_upper.isChecked():
            words.append(string.ascii_uppercase*2)
        if self.checkBox_lower.isChecked():
            words.append(string.ascii_lowercase*2)    
        if self.checkBox_digit.isChecked():
            words.append(string.digits*2)
        if self.checkBox_p.isChecked():
            words.append(string.punctuation*2)
        #只生成数字密码
        # words=(string.digits)
        if not words:
            words=(string.ascii_letters
                +string.digits
                +string.punctuation
                +string.ascii_uppercase+string.ascii_lowercase)
        else:
            words="".join(words)
        passwords=random.sample(list(words),10)
        passwords="".join(passwords)
        self.lineEdit.setText(passwords)
        with open("./password.txt","a",encoding="utf-8") as f:
            f.write(site+":"+passwords+"\n")
        
        #加入提示信息   
        QMessageBox.information(self,"提示","密码生成成功")  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = mycodegenerate()
    dialog.show()
    sys.exit(app.exec())