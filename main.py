from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

# MainWindow class handles the functionality of the notepad application
class MainWindow(QMainWindow):

    # Constructor initializes the main window and loads the .ui file
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('editor.ui', self)  # Load the UI layout from an external file
        self.show()  # Display the main window

        # Set the title of the window
        self.setWindowTitle('Notepad')

        # Connect menu actions to change text size in the editor
        self.action12_pt.triggered.connect(lambda: self.change_size(12))
        self.action18_pt.triggered.connect(lambda: self.change_size(18))
        self.action24_pt.triggered.connect(lambda: self.change_size(24))

        # Connect the "Open" action to the method that opens files
        self.actionOpen.triggered.connect(self.open_file)

    # Method to change the font size of the text editor
    def change_size(self, size):
        self.plainTextEdit.setFont(QFont('Arial', size))

    # Method to open and display a file in the text editor
    def open_file(self):
        options = QFileDialog.Options()
        # Open the file dialog with filters for text and Python files
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', "", "Text Files (*.txt);;Python Files (*.py)", options=options)
        if filename != "":
            with open(filename, 'r') as f:
                # Set the content of the file in the text editor
                self.plainTextEdit.setPlainText(f.read())

# Main function to run the application
def main():
    app = QApplication([])  # Create the application instance
    window = MainWindow()   # Create and display the main window
    app.exec_()  # Start the event loop

# Entry point for the script
if __name__ == '__main__':
    main()
