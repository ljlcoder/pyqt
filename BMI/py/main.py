from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from bmi import Ui_Dialog as bmi
import string
import random
class mybmi(bmi,QDialog):
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

        self.pushButton.clicked.connect(self.show_compute_bmi)

    def show_compute_bmi(self):
        """
        Slot method to compute the BMI.
        
        This method is connected to the button clicked signal and computes the
        BMI of the user. The BMI is then set as the text of the line edit
        widget. Finally, a message box pops up with the message " " (Password
        generated successfully).
        """
        if self.weight.text()=="" or self.height.text()=="":
            QMessageBox.warning(self,"警告","请输入体重和身高") 
            return
        try:
            weight=float(self.weight.text())
            height=float(self.height.text())/100
        except:
            QMessageBox.warning(self,"警告","请输入数字")
            return  
        
        bmi=round(weight/(height**2),2)
        ideal=round(22*(height**2),2)
        res_text=f"BMI:{bmi},理想体重是{ideal}KG"
        self.res.setText(res_text)
        
        QMessageBox.information(self,"提示","计算成功")
        # with open("bmi.txt","a",encoding="utf-8") as f:
        #     f.write(self.lineEdit.text()+"\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = mybmi()
    dialog.show()
    sys.exit(app.exec())