import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Nointernet(QMainWindow):
    def __init__(self, image_folder):
        super().__init__()
        self.label = QLabel()
        self.label.setText("hhhfggg")
        self.setCentralWidget(self.label)
        self.setWindowTitle("No Internet")
        self.set
        

if __name__ == "__main__":
    app = QApplication([])
    folder_path = "images/Ruto"  # Replace with your image folder path
    window = Nointernet(folder_path)
    window.show()
    app.exec_()
