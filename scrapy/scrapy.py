# Form implementation generated from reading ui file 'scrapy.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_scarpy(object):
    def setupUi(self, scarpy):
        scarpy.setObjectName("scarpy")
        scarpy.resize(674, 554)
        scarpy.setStyleSheet("* {\n"
"    font-size:18px;\n"
"}\n"
"QPushButton{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rgb(0, 170, 255);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(scarpy)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=scarpy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_url = QtWidgets.QLineEdit(parent=scarpy)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout.addWidget(self.lineEdit_url)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(parent=scarpy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=scarpy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_num = QtWidgets.QLineEdit(parent=scarpy)
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.horizontalLayout_2.addWidget(self.lineEdit_num)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(parent=scarpy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.progressBar = QtWidgets.QProgressBar(parent=scarpy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.pushButton_save = QtWidgets.QPushButton(parent=scarpy)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)

        self.retranslateUi(scarpy)
        QtCore.QMetaObject.connectSlotsByName(scarpy)

    def retranslateUi(self, scarpy):
        _translate = QtCore.QCoreApplication.translate
        scarpy.setWindowTitle(_translate("scarpy", "小说爬取器"))
        self.label.setText(_translate("scarpy", "请输入爬取的url："))
        self.pushButton.setText(_translate("scarpy", "执行爬虫"))
        self.label_2.setText(_translate("scarpy", "统计信息"))
        self.pushButton_save.setText(_translate("scarpy", "保存文件"))