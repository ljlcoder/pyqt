# Form implementation generated from reading ui file 'json.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Json(object):
    def setupUi(self, Json):
        Json.setObjectName("Json")
        Json.resize(690, 565)
        self.verticalLayout = QtWidgets.QVBoxLayout(Json)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Json)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(parent=Json)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.string = QtWidgets.QPushButton(parent=Json)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.string.setFont(font)
        self.string.setObjectName("string")
        self.horizontalLayout.addWidget(self.string)
        self.f_string = QtWidgets.QPushButton(parent=Json)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.f_string.setFont(font)
        self.f_string.setObjectName("f_string")
        self.horizontalLayout.addWidget(self.f_string)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.copy = QtWidgets.QPushButton(parent=Json)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.copy.setFont(font)
        self.copy.setObjectName("copy")
        self.verticalLayout.addWidget(self.copy)

        self.retranslateUi(Json)
        QtCore.QMetaObject.connectSlotsByName(Json)

    def retranslateUi(self, Json):
        _translate = QtCore.QCoreApplication.translate
        Json.setWindowTitle(_translate("Json", "Json格式化"))
        self.label.setText(_translate("Json", "请粘贴JSON文本:"))
        self.string.setText(_translate("Json", "格式化字符串"))
        self.f_string.setText(_translate("Json", "反格式化字符串"))
        self.copy.setText(_translate("Json", "复制内容"))
