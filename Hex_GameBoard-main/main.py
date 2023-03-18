import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from game import Ui_MainWindow


class Gex(QMainWindow):
    def __init__(self):
        super(Gex, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gex()
    window.show()

    sys.exit(app.exec())
