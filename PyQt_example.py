import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 240, 180)
        self.setWindowTitle('pyqt5 tutorials')
        self.home()

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(100, 30)
        btn.move(10, 10)
        self.show()

def run():
	app = QApplication(sys.argv)
	frame = window()
	sys.exit(app.exec_())

run()