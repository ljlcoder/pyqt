from PyQt6.QtWidgets import (QApplication,QDialog,QMessageBox,QPushButton,QLabel,QVBoxLayout)
import sys
import time
class Mytimereducer(QDialog):
    def __init__(self):
        super().__init__()
        self.show()
        self.btn0 = QPushButton("start", self)
        self.label0=QLabel("10",self)
        self.btn0.clicked.connect(self.do_reducer)
        self.btn1 = QPushButton("auto", self)
        self.label1=QLabel("10",self)
        self.btn1.clicked.connect(self.do_reducer1)
        layout=QVBoxLayout()
        layout.addWidget(self.btn0)
        layout.addWidget(self.label0)
        layout.addWidget(self.btn1)
        layout.addWidget(self.label1)

        self.setLayout(layout)
    def do_reducer(self):
        new_value=int(self.label0.text())-1
        self.label0.setText(str(new_value))
    def do_reducer1(self):
        """
        Auto reduce the value of label1 by 1 every time until 0.
        """
        while 1:
            new_value=int(self.label1.text())-1
            self.label1.setText(str(new_value))
            time.sleep(1)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Mytimereducer()
    dialog.show()
    sys.exit(app.exec())