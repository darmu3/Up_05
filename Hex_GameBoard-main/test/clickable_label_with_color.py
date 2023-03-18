import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QWidget, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.label.installEventFilter(self)
        self.label.setStyleSheet("min-width: 20px; min-height: 20px; border: 1px solid #444; background-color:Yellow")

        layout = QHBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)

    def eventFilter(self, obj, e):
        if e.type() == 2:
            btn = e.button()
            if btn == 1:
                self.label.setStyleSheet("background-color: Green")
            elif btn == 2:
                self.label.setStyleSheet("background-color: Blue")
        return super(QWidget, self).eventFilter(obj, e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())