from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys
from post import Ui_Dialog
import json
import requests
class my_ui_post(Ui_Dialog,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.retranslateUi(self)
        self.summit.clicked.connect(self.submmit)
    def submmit(self):
        method=self.request.currentText()
        url=self.url.text()
        headers=self.textEdit_headers.toPlainText()
        params=self.textEdit_params.toPlainText()
        data=self.textEdit_data.toPlainText()
        if not method:
            QMessageBox.warning(self,"警告","请选择请求方法")
            return
        if not url:
            QMessageBox.warning(self,"警告","请输入URL")
            return
        # if not headers:
        #     QMessageBox.warning(self,"警告","请输入请求头")
        #     return
        # if not params:
        #     QMessageBox.warning(self,"警告","请输入参数")
        #     return
        # if not data:
        #     QMessageBox.warning(self,"警告","请输入数据")
        #     return
        try:
            headers=json.loads(headers)
        except:
            QMessageBox.warning(self,"警告","请输入正确的请求头")
            return
        try:
            params=json.loads(params)
        except:
            QMessageBox.warning(self,"警告","请输入正确的参数")
            return
        try:
            data=json.loads(data)
        except:
            QMessageBox.warning(self,"警告","请输入正确的数据")
        if method=="GET":
            res=requests.get(url=url,params=params,headers=headers)
        else:
            res=requests.post(url=url,data=json.dumps(data),headers=headers)
        code=res.status_code
        text=res.text
        result=""
        result+=f'code:{code}\n'
        result+=f'content:{text}\n'
        self.res.setPlainText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_post()
    dialog.show()
    sys.exit(app.exec())


"""
{"sites": {"site": [{"id": "1", "name": "菜鸟教程", "url": "www.runoob.com"}, {"id": "2", "name": "菜鸟工具", "url": "www.jyshare.com"}, {"id": "3", "name": "Google", "url": "www.google.com"}]}}
"""