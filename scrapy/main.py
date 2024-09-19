from PyQt6.QtWidgets import (QListWidgetItem,QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox,QFileDialog)    
import sys
from scrapy import Ui_scarpy
from demo import get_chapter,get_content
from PyQt6 import QtCore
import os
class my_ui_scarpy(Ui_scarpy,QDialog):
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
        self.pushButton.clicked.connect(self.exec_scrapy)
        self.pushButton_save.clicked.connect(self.load_save)

    def exec_scrapy(self):
        root_url=self.lineEdit_url.text().strip()
        if root_url == "":
            QMessageBox.warning(self,"警告","请输入URL")
            return
        #统计爬虫信息
        chapter=get_chapter(root_url)
        self.res=[]
        self.lineEdit_num.setText(str(len(chapter)))
        self.worker=MySpiderThread(chapter=chapter)
        self.worker.start()
        self.worker.my_signal.connect(self.update_log)
        self.listWidget.clear()
        self.listWidget.addItems(self.lineEdit_num.text().split("\n"))
    def update_log(self,data):
        href=data["href"]
        title=data["title"]
        item=QListWidgetItem(f"{title} {href}")
        self.listWidget.addItem(item)
        # self.progressBar.setValue(0)
        self.res.append(data)
        value=int(100*len(self.res)/len(self.chapter))
        self.progressBar.setValve(value)
    def load_save(self):
        filepath,filetype=QFileDialog.getSaveFileName(self,"保存",os.getcwd(),"*.txt")
        if filepath == "":
            return
        with open(filepath,"a",encoding="utf-8") as f:
            for data in self.res:
                f.write(data["href"]+"\n")
                f.write(data["title"]+"\n")
                f.write(data["data"]+"\n")
        # if self.lineEdit_url.text() == "":
        #     return
        # with open("./scrapy.txt","a",encoding="utf-8") as f:
        #     f.write(self.listWidget.text())
        QMessageBox.information(self,"提示","保存成功")

class MySpiderThread(QtCore.QThread):
    """
    自定义线程类，继承自QThread
    """
    my_signal = QtCore.pyqtSignal(str)
    def __init__(self, chapter, parent=None):
        super(MySpiderThread, self).__init__(parent)  
        self.chapter = chapter
    def run(self):
        for chapter in self.chapter:
            href=chapter["href"]
            title=chapter["title"]
            res=get_content(href)
            data={
                "href":href,
                "titile":title,
                "data":data
            }
            self.my_signal.emit(str(data))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = my_ui_scarpy()
    dialog.show()
    sys.exit(app.exec())


"""
{"sites": {"site": [{"id": "1", "name": "菜鸟教程", "url": "www.runoob.com"}, {"id": "2", "name": "菜鸟工具", "url": "www.jyshare.com"}, {"id": "3", "name": "Google", "url": "www.google.com"}]}}
"""