# Form implementation generated from reading ui file '.\excel.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Excel(object):
    def setupUi(self, Excel):
        Excel.setObjectName("Excel")
        Excel.resize(547, 491)
        Excel.setStyleSheet("* {\n"
"    font-size:18px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Excel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Excel)
        self.label.setStyleSheet("* {\n"
"    font-size:18px;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.excel_dir = QtWidgets.QLineEdit(parent=Excel)
        self.excel_dir.setObjectName("excel_dir")
        self.horizontalLayout.addWidget(self.excel_dir)
        self.choose_file = QtWidgets.QPushButton(parent=Excel)
        self.choose_file.setObjectName("choose_file")
        self.horizontalLayout.addWidget(self.choose_file)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=Excel)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(parent=Excel)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(parent=Excel)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.output_dir = QtWidgets.QLineEdit(parent=Excel)
        self.output_dir.setObjectName("output_dir")
        self.horizontalLayout_3.addWidget(self.output_dir)
        self.choose_dir = QtWidgets.QPushButton(parent=Excel)
        self.choose_dir.setObjectName("choose_dir")
        self.horizontalLayout_3.addWidget(self.choose_dir)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.do_split = QtWidgets.QPushButton(parent=Excel)
        self.do_split.setObjectName("do_split")
        self.verticalLayout.addWidget(self.do_split)

        self.retranslateUi(Excel)
        QtCore.QMetaObject.connectSlotsByName(Excel)

    def retranslateUi(self, Excel):
        _translate = QtCore.QCoreApplication.translate
        Excel.setWindowTitle(_translate("Excel", "Excel"))
        self.label.setText(_translate("Excel", "请选择Excel文件:"))
        self.choose_file.setText(_translate("Excel", "选择Excel文件"))
        self.label_2.setText(_translate("Excel", "选择要拆分的列:"))
        self.comboBox.setItemText(0, _translate("Excel", "**无**"))
        self.label_3.setText(_translate("Excel", "选择要输出的列:"))
        self.choose_dir.setText(_translate("Excel", "选择输出的目录"))
        self.do_split.setText(_translate("Excel", "进行拆分"))
