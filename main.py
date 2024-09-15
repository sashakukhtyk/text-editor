from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show()

        self.setWindowTitle('Notepad')
        self.action12_pt.triggered.connect(lambda: self.change_size(12))
        self.action18_pt.triggered.connect(lambda: self.change_size(18))
        self.action24_pt.triggered.connect(lambda: self.change_size(24))

    def change_size(self, size):
        self.plainTextEdit.setFont(QFont('Arial', size))



def main():
    app = QApplication([])
    window = MainWindow()
    app.exec_()


if __name__ == '__main__':
    main()
