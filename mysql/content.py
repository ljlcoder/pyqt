# Form implementation generated from reading ui file 'content.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_content(object):
    def setupUi(self, content):
        content.setObjectName("content")
        content.resize(727, 450)
        content.setStyleSheet("* {\n"
"    font-size:18px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(content)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=content)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=content)
        self.plainTextEdit.setStyleSheet("* {\n"
"    font-size:18px;\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=content)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(parent=content)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=content)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(parent=content)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_commit = QtWidgets.QPushButton(parent=content)
        self.pushButton_commit.setObjectName("pushButton_commit")
        self.verticalLayout.addWidget(self.pushButton_commit)

        self.retranslateUi(content)
        QtCore.QMetaObject.connectSlotsByName(content)

    def retranslateUi(self, content):
        _translate = QtCore.QCoreApplication.translate
        content.setWindowTitle(_translate("content", "Content"))
        self.label.setText(_translate("content", "代办内容:"))
        self.label_2.setText(_translate("content", "截止日期:"))
        self.label_3.setText(_translate("content", "完成状态:"))
        self.comboBox.setItemText(0, _translate("content", "未完成"))
        self.comboBox.setItemText(1, _translate("content", "已完成"))
        self.comboBox.setItemText(2, _translate("content", "进行中"))
        self.pushButton_commit.setText(_translate("content", "提交数据"))
