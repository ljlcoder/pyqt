# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(717, 541)
        Login.setStyleSheet("* {\n"
"    font-size:18px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Login)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Login)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=Login)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_username = QtWidgets.QLineEdit(parent=Login)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout.addWidget(self.lineEdit_username)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=Login)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_password = QtWidgets.QLineEdit(parent=Login)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_login = QtWidgets.QPushButton(parent=Login)
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout.addWidget(self.pushButton_login)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登陆表"))
        self.label.setText(_translate("Login", "请登录"))
        self.label_2.setText(_translate("Login", "请输入用户名:"))
        self.label_3.setText(_translate("Login", "请输入密码:"))
        self.pushButton_login.setText(_translate("Login", "登录"))