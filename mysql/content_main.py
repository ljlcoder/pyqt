from PyQt6.QtWidgets import (QListWidgetItem,QFileDialog,QTableWidgetItem,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
from content import Ui_content
import sys
class my_ui_content(Ui_content,QDialog):
    def __init__(self,conn,userid,username):
        """
        Constructor method
        
        Calls the constructor of the base class, then sets up the UI and
        translates it. Finally, it connects the button to the slot method
        show_new_password.
        """
        super().__init__()
        self.setupUi(self)  
        self.retranslateUi(self)
        self.conn=conn
        self.userid=userid
        self.username=username

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_content()
    dialog.show()
    sys.exit(app.exec())
