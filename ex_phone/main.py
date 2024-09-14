from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from phone import Ui_ex_phone
import re
class my_ex_phone(Ui_ex_phone,QDialog):
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
        self.extract.clicked.connect(self.extract_phone)
        self.copy.clicked.connect(self.copy_phone_list)

    def extract_phone(self):    
        """
        Slot method to extract phone numbers from the input text.
        
        This method is connected to the button clicked signal and extracts
        phone numbers from the input text. The extracted phone numbers are
        then set as the text of the text edit widget. If the input text is
        empty, a message box pops up with the message " " (Please enter
        the correct content). If no phone numbers are found, a message box
        pops up with the message " " (No phone numbers found).
        """
        text=self.textEdit.toPlainText()    
        if text=="":
            QMessageBox.warning(self,"警告","请输入要提取的内容")
            return
        #用正则表达式提取电话号码
        pattern = re.compile(r'1[3456789]\d{9}')
        result = pattern.findall(text)
        if len(result)==0:
            QMessageBox.warning(self,"警告","没有找到电话号码")
            return
        self.textEdit_2.setPlainText("\n".join(result))
    def copy_phone_list(self):
        """
        Slot method to copy the phone numbers to the clipboard.
        
        This method is connected to the button clicked signal and copies the
        phone numbers in the text edit widget to the clipboard. If the text
        edit widget is empty, a message box pops up with the message " "
        (No phone numbers found). If the phone numbers are copied successfully,
        a message box pops up with the message " " (Copy successfully).
        """
        text=self.textEdit_2.toPlainText()
        if text=="":
            QMessageBox.warning(self,"警告","没有找到电话号码")
            return
        QApplication.clipboard().setText(text)
        QMessageBox.information(self,"提示","复制成功")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ex_phone()
    dialog.show()
    sys.exit(app.exec())


'''
19989881888
15619292345
'''