# Form implementation generated from reading ui file '.\docx_search.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(747, 555)
        Search.setStyleSheet("* {\n"
"    font-size:18px;\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Search)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.choose = QtWidgets.QPushButton(parent=Search)
        self.choose.setObjectName("choose")
        self.horizontalLayout.addWidget(self.choose)
        self.lineEdit_dir = QtWidgets.QLineEdit(parent=Search)
        self.lineEdit_dir.setText("")
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.horizontalLayout.addWidget(self.lineEdit_dir)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_search = QtWidgets.QLineEdit(parent=Search)
        self.lineEdit_search.setText("")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_2.addWidget(self.lineEdit_search)
        self.search = QtWidgets.QPushButton(parent=Search)
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(parent=Search)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.open = QtWidgets.QPushButton(parent=Search)
        self.open.setObjectName("open")
        self.verticalLayout.addWidget(self.open)

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("Search", "文档搜集神器"))
        self.choose.setText(_translate("Search", "请选择目录"))
        self.search.setText(_translate("Search", "搜索"))
        self.open.setText(_translate("Search", "打开选中文件夹"))