from PyQt6.QtWidgets import (QApplication,QDialog,QPushButton,QHBoxLayout,QMessageBox)    
import sys

# 创建应用
# 创建对话框
# 创建水平布局
# 创建按钮
# 将按钮添加到布局中
# 将布局添加到对话框中
# 显示对话框
# 退出应用

def show_msg():
    QMessageBox.information(dialog,"msg","hello world")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = QDialog()
    dialog.resize(300,400)
    hbox=QHBoxLayout()
    button=QPushButton("click me",dialog)
    button.clicked.connect(show_msg)
    hbox.addWidget(button)
    dialog.setLayout(hbox)
    dialog.show()
    sys.exit(app.exec())  


