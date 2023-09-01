import sys
from tkinter import Widget

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot

def window():

    # initialization
    app = QApplication(sys.argv)
    widget = QWidget()
    textLabel = QLabel(widget)

    # text formatting
    textLabel.setText('Hello Master')
    textLabel.move(170, 120)

    # windows formatting
    widget.setGeometry(0, 0, 400, 300)
    widget.setWindowTitle("EXAMPLE")
    
    # to show the window
    widget.show()
    
    # to exit the window
    sys.exit(app.exec())


if __name__ == '__main__':
    window()