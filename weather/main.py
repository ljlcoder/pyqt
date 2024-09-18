from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox,QFileDialog)    
import sys
from weather import Ui_Dialog
import pandas as pd
import os
import matplotlib.pyplot as plt
class my_ui_weather(Ui_Dialog,QDialog):
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
        self.pushButton.clicked.connect(self.load_excel)
        self.pushButton_2.clicked.connect(self.draw_chart)
        # self.df=pd.read_excel("./10年的北京天气数据.xlsx")
    def load_excel(self):
        self.filepath,filetype=QFileDialog.getOpenFileName(self,"请选择Excel",os.getcwd(),"Excel files(*.xlsx *.xls)")
        dfs=pd.read_excel(self.filepath,sheet_name=None)
        sheets_name=list(dfs.keys())
        self.comboBox.clear()
        self.comboBox.addItems(sheets_name)
    def draw_chart(self):
        year=self.comboBox.currentText()
        if not self.filepath or "请选择年份" in year:
            return
        df=pd.read_excel(self.filepath,sheet_name=year)
        x=df['日期'].map(lambda x:x.split()[0])
        high=df["最高温"].map(lambda y:y.replace("°C","").strip())
        low=df["最低温"].map(lambda y:y.replace("°C",""))
        self.widget.axes.clear()
        self.widget.axes.plot(x,high)
        self.widget.draw()

        df_agg=df["天气"].value_counts()
        size=list(df_agg)
        labels=list(df_agg.index)
        # 中文设置字体
        plt.rcParams["font.sans-serif"] = ["SimHei"]
        # 该语句解决图像中的“-”负号的乱码问题
        plt.rcParams["axes.unicode_minus"] = False
 
        self.widget_2.axes.clear()
        self.widget_2.axes.pie(size[:20],labels=labels[:20])
        self.widget_2.draw()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_weather()
    dialog.show()
    sys.exit(app.exec())


"""
{"sites": {"site": [{"id": "1", "name": "菜鸟教程", "url": "www.runoob.com"}, {"id": "2", "name": "菜鸟工具", "url": "www.jyshare.com"}, {"id": "3", "name": "Google", "url": "www.google.com"}]}}
"""