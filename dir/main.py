from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from  my_dir import Ui_dir
class my_ui_dir(Ui_dir,QDialog):
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
        self.select.clicked.connect(self.select_dir)
        self.start.clicked.connect(self.start_dir)
        self.open_dir.clicked.connect(self.open_dirs)
    def select_dir(self):
    
        pass
    def start_dir(self):
        pass
    def open_dirs(self):
        """
        Slot method to open a directory dialog to select the directory to search for in.

        This method is connected to the button clicked signal and opens a directory dialog
        to select the directory to search for in. The selected directory is then set as
        the text of the line edit widget.
        """
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_dir()
    dialog.show()
    sys.exit(app.exec())
