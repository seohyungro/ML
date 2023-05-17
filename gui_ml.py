from PyQt5.QtWidgets import *
import sys , pickle

from PyQt5 import uic, QtCore, QtGui

class UI(QMainWindow):
    def __init(self):
        super(UI, self).__init__()
        uic.loadUi("./mainwindow.ui", self)
        self.show()

if __name__ == '__main__': # if __name__ == 사용하면 이 제일 먼저 실행됨
    app = QApplication(sys.argv)
    window = UI()
    app.exec_()
