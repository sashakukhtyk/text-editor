from PyQt5.QtWidgets import *
from PyQt5 import uic


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show()


def main():
    app = QApplication([])
    window = MainWindow()
    app.exec_()


if __name__ == '__main__':
    main()
