# Form implementation generated from reading ui file 'schedule.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_schedule(object):
    def setupUi(self, schedule):
        schedule.setObjectName("schedule")
        schedule.resize(664, 523)
        self.verticalLayout = QtWidgets.QVBoxLayout(schedule)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=schedule)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_add = QtWidgets.QPushButton(parent=schedule)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_change = QtWidgets.QPushButton(parent=schedule)
        self.pushButton_change.setObjectName("pushButton_change")
        self.horizontalLayout.addWidget(self.pushButton_change)
        self.pushButton_delete = QtWidgets.QPushButton(parent=schedule)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout.addWidget(self.pushButton_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_export = QtWidgets.QPushButton(parent=schedule)
        self.pushButton_export.setObjectName("pushButton_export")
        self.verticalLayout.addWidget(self.pushButton_export)

        self.retranslateUi(schedule)
        QtCore.QMetaObject.connectSlotsByName(schedule)

    def retranslateUi(self, schedule):
        _translate = QtCore.QCoreApplication.translate
        schedule.setWindowTitle(_translate("schedule", "代办数据管理"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("schedule", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("schedule", "代办内容"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("schedule", "截止日期"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("schedule", "创建时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("schedule", "完成状态"))
        self.pushButton_add.setText(_translate("schedule", "新增代办项"))
        self.pushButton_change.setText(_translate("schedule", "更改代办项"))
        self.pushButton_delete.setText(_translate("schedule", "删除代办项"))
        self.pushButton_export.setText(_translate("schedule", "导出列表"))
