from PyQt6.QtWidgets import (QFileDialog,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from  my_dir import Ui_dir
import os
import shutil
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
        self.file_dir_path=""
        self.retranslateUi(self)
        self.select.clicked.connect(self.select_dir)
        self.start.clicked.connect(self.start_dir)
        self.open_dir.clicked.connect(self.open_dirs)
    def select_dir(self):
        self.filedir_path=QFileDialog.getExistingDirectory(self,"选择文件夹",os.getcwd())
        if self.filedir_path=="":
            return
        self.lineEdit.setText(self.filedir_path)
    def start_dir(self):
        file_dir=self.lineEdit.text()
        for fname in os.listdir(file_dir):
            if os.path.isdir(os.path.join(file_dir, fname)):
                continue
            ext_name=fname.split(".")[-1].strip()
            ext_dir=os.path.join(file_dir,ext_name)
            if not os.path.exists(ext_dir):
                os.mkdir(ext_dir)
            shutil.move(os.path.join(file_dir, fname),ext_dir)
        QMessageBox.information(self,"提示","扫描完成")

    def open_dirs(self):
        """
        Slot method to open a directory dialog to select the directory to search for in.

        This method is connected to the button clicked signal and opens a directory dialog
        to select the directory to search for in. The selected directory is then set as
        the text of the line edit widget.
        """
        if not os.path.isdir(self.lineEdit.text()):
            QMessageBox.warning(self,"警告","请先选择文件夹")
            return
        os.startfile(self.lineEdit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_dir()
    dialog.show()
    sys.exit(app.exec())
