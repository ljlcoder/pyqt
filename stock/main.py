from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from stock_ui import Ui_stock
from stock_data import get_data,get_single_data
import pyqtgraph as pg
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
        self.plot_item=self.widget_qtgraph.getPlotItem()
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
        stocks=get_data()
        stocks_data=[]
        for idx,row in stocks.iterrows():
            code=row['code']
            code_name=row['code_name']
            code_str=f"{code}#{code_name}"
            stocks_data.append(code_str)
        self.comboBox_select.clear()
        self.comboBox_select.addItems(stocks_data)
    def loading(self):        
        code_str=self.comboBox_select.currentText()
        if "#" not in code_str:
            return
        code=code_str.split("#")[0]
        stock_data_list=get_single_data(code,"2020-01-01","2022-01-01")
        date=stock_data_list["date"]
        close=stock_data_list["close"].astype(float)
        x_dict=dict(enumerate(date))
        pg.AxisItem(orientation='bottom').setTicks([x_dict.items()])
        self.plot_item.setAxisItems({"bottom": pg.AxisItem(orientation='bottom')})
        self.plot_item.plot(list(x_dict.keys()),close,pen=pg.mkPen(color=(255, 0, 0), width=3),clear=True)
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
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_stock()
    dialog.show()
    sys.exit(app.exec())


"""
{"sites": {"site": [{"id": "1", "name": "菜鸟教程", "url": "www.runoob.com"}, {"id": "2", "name": "菜鸟工具", "url": "www.jyshare.com"}, {"id": "3", "name": "Google", "url": "www.google.com"}]}}
"""