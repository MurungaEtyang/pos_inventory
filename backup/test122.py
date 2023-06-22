from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import subprocess
import sys

class show_Dataset(QWidget):
    def __init__(self, parent=None):
        super(show_Dataset, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("Administrative Dashboard")
        self.setWindowFlags(Qt.WindowMaximized)
        
        # Fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        
        # Header
        self.label = QLabel(self)
        self.label.setText("Welcome to the Administrative Dashboard")
        self.label.move(20, 20)
        self.label.setFont(font)
        self.label.setFixedHeight(70)

def main():
    app = QApplication(sys.argv)
    app1 = show_Dataset()
    app1.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
