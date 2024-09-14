from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from stock_ui import Ui_stock


class my_ui_stock(Ui_stock,QDialog):
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
        self.pushButton_load.clicked.connect(self.load)
        self.pushButton_loading.clicked.connect(self.loading)
        # self.comboBox_select.clicked.connect(self.select)
        self.widget_qtgraph.mousePressEvent = self.mousePressEvent
    def select(self):
        pass
    def load(self):
        """
        Slot method to load stock data from a file.

        This method is connected to the button clicked signal and loads
        stock data from a file. The loaded data is then plotted in the
        qtgraph widget.

        """
        
        pass
    def loading(self):        
        pass
    def mousePressEvent(self, event):
        """
        Mouse press event handler for the qtgraph widget.

        This method is connected to the mouse press event of the qtgraph widget.
        It is called when the user clicks on the qtgraph widget.

        Parameters
        ----------
        event : QMouseEvent
            The mouse event object.

        Returns
        -------
        None

        """
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_stock()
    dialog.show()
    sys.exit(app.exec())


"""
{"sites": {"site": [{"id": "1", "name": "菜鸟教程", "url": "www.runoob.com"}, {"id": "2", "name": "菜鸟工具", "url": "www.jyshare.com"}, {"id": "3", "name": "Google", "url": "www.google.com"}]}}
"""