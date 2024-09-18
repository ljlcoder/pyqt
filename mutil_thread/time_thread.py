from PyQt6.QtWidgets import (QApplication,QDialog,QMessageBox,QPushButton,QLabel,QVBoxLayout)
from PyQt6.QtCore import QThread,pyqtSignal
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
        self.worker=Mytimethread(self.label1.text())
        self.worker.my_signal.connect(self.update_value)
        self.btn1.clicked.connect(self.do_reducer1)
        layout=QVBoxLayout()
        layout.addWidget(self.btn0)
        layout.addWidget(self.label0)
        layout.addWidget(self.btn1)
        layout.addWidget(self.label1)

        self.setLayout(layout)
    def do_reducer(self):
        new_value=int(self.label0.text())-1
        if new_value < 0:
            new_value=10
        self.label0.setText(str(new_value))
    def do_reducer1(self):
        """
        Auto reduce the value of label1 by 1 every time until 0.
        """
        if self.worker.isRunning():
            return
        self.worker.start()
    def update_value(self,new_value):
        self.label1.setText(str(new_value))
class Mytimethread(QThread):
    my_signal=pyqtSignal(int)
    def __init__(self,value):
        super().__init__()
        self.value=value
    def run(self):
        while 1:
            self.value=int(self.value)-1
            if self.value < 0:
                self.value=10
            self.my_signal.emit(self.value)
            time.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Mytimereducer()
    dialog.show()
    sys.exit(app.exec())