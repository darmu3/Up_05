from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Python ")
		self.setGeometry(100, 100, 600, 400)
		self.UiComponents()
		self.show()

	def UiComponents(self):
		button = QPushButton("CLICK", self)
		button.setGeometry(200, 150, 100, 30)
		button.clicked.connect(self.clickme)
	def clickme(self):
		print('Окно закрыто')
		self.Window.close

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
