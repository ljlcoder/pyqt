from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from myjson import Ui_Json
import string
import random
import json

class my_ui_json(Ui_Json,QDialog):
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
        self.string.clicked.connect(self.show_string)
        self.f_string.clicked.connect(self.show_f_string)
        self.copy.clicked.connect(self.copy_to_clipboard)
    def show_string(self):
        text=self.textEdit.toPlainText()
        if text=="":
            QMessageBox.warning(self,"警告","请输入JSON文本")
            return
        try:
            text=json.dumps(json.loads(text),indent=4,ensure_ascii=False)
            self.textEdit.setPlainText(text)
        except:
            QMessageBox.warning(self,"警告","请输入正确的JSON文本")
            return
    def show_f_string(self):
        """
        Slot method to format the string as a JSON object.
        
        This method is connected to the button clicked signal and formats the
        string in the text edit widget as a JSON object. The formatted string is
        then set as the text of the text edit widget. If the string is not a valid
        JSON object, a message box pops up with the message " " (Please enter
        the correct JSON text).
        """
        text=self.textEdit.toPlainText()
        if text=="":
            QMessageBox.warning(self,"警告","请输入JSON文本")
            return
        try:
            text=json.dumps(json.loads(text),ensure_ascii=False)
            self.textEdit.setPlainText(text)
        except:
            QMessageBox.warning(self,"警告","请输入正确的JSON文本")
            return
    def copy_to_clipboard(self):
        """
        Slot method to copy the text in the text edit widget to the clipboard.

        This method is connected to the button clicked signal and copies the
        text in the text edit widget to the clipboard. A message box pops up with
        the message " " (Copy successfully).
        """
        QApplication.clipboard().setText(self.textEdit.toPlainText())
        QMessageBox.information(self,"提示","复制成功")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_json()
    dialog.show()
    sys.exit(app.exec())


"""
{"sites": {"site": [{"id": "1", "name": "菜鸟教程", "url": "www.runoob.com"}, {"id": "2", "name": "菜鸟工具", "url": "www.jyshare.com"}, {"id": "3", "name": "Google", "url": "www.google.com"}]}}
"""