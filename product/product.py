# Form implementation generated from reading ui file '.\product.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_product(object):
    def setupUi(self, product):
        product.setObjectName("product")
        product.resize(697, 529)
        product.setStyleSheet("* {\n"
"    font-size:16px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rgb(0, 170, 255);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(product)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=product)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(parent=product)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pie = QtWebEngineWidgets.QtWebEngineView(parent=product)
        self.pie.setObjectName("pie")
        self.verticalLayout.addWidget(self.pie)
        self.label_2 = QtWidgets.QLabel(parent=product)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.bar = QtWebEngineWidgets.QtWebEngineView(parent=product)
        self.bar.setObjectName("bar")
        self.verticalLayout.addWidget(self.bar)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 8)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 8)

        self.retranslateUi(product)
        QtCore.QMetaObject.connectSlotsByName(product)

    def retranslateUi(self, product):
        _translate = QtCore.QCoreApplication.translate
        product.setWindowTitle(_translate("product", "订单统计图设计"))
        self.pushButton.setText(_translate("product", "请输入订单数据文件"))
        self.label.setText(_translate("product", "利润占比饼状图"))
        self.label_2.setText(_translate("product", "利润占比柱状图"))
from PyQt6 import QtWebEngineWidgets