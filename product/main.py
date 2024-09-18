from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox,QFileDialog)    
import sys
from product import Ui_product
import pandas as pd
import os
import plotly.express as px
class my_ui_product(Ui_product,QDialog):
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
    def load_excel(self):
        filepath,filetype=QFileDialog.getOpenFileName(self,"请选择Excel",os.getcwd(),"Excel files(*.xlsx *.xls)")
        df=pd.read_excel(filepath)
        df_agg=df.groupby("产品名称").apply(lambda x:pd.Series({"销售利润":sum(x["销售利润(元)"])})).reset_index()
        df.agg.columns=["产品名称","销售利润(元)"]
        fig=px.pie(df_agg,values="销售利润",names="产品名称",title="饼状图")
        html = fig.to_html(include_plotlyjs="cdn")
        html = html.replace(
            "https://cdn.plot.ly/plotly-2.12.1.min.js",
            "https://cdn.bootcdn.net/ajax/libs/plotly.js/2.14.0/plotly-basic.min.js"
        )
        self.pie.setHtml(html)
        fig=px.bar(df_agg,x='产品名称',y='销售利润(元)',title="柱状图")
        html_2 = fig.to_html(include_plotlyjs="cdn")
        html_2 = html_2.replace(
            "https://cdn.plot.ly/plotly-2.12.1.min.js",
            "https://cdn.bootcdn.net/ajax/libs/plotly.js/2.14.0/plotly-basic.min.js"
        )
        self.bar.setHtml(html_2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_product()
    dialog.show()
    sys.exit(app.exec())


"""
{"sites": {"site": [{"id": "1", "name": "菜鸟教程", "url": "www.runoob.com"}, {"id": "2", "name": "菜鸟工具", "url": "www.jyshare.com"}, {"id": "3", "name": "Google", "url": "www.google.com"}]}}
"""