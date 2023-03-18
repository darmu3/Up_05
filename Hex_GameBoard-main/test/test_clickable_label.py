from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow

class W(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.label = QLabel('Label')
        self.flag = True
        self.setCentralWidget(self.label)
        self.label.installEventFilter(self)

    def eventFilter(self, obj, e):
        if e.type() == 2:
            btn = e.button()
            if btn == 1:
                self.label.setText('Clicked Left Button')
            elif btn == 2:
                self.label.setText('Clicked Right Button')
        return super(QMainWindow, self).eventFilter(obj, e)


app = QApplication([])
w = W()
w.show()
app.exec_()