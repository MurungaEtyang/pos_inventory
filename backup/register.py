from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import login
import sys

class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.resize(2000,1000)
        self.setWindowTitle("Register")
        # label 1 (header)
        self.label = QLabel(self)
        self.label.setText("Welcome to registration") 
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.move(550,10)

        # label 2
        self.label2 = QLabel(self)
        self.label2.setText("Enter your First Name")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(True)
        font2.setCapitalization(True)
        self.label2.setFont(font2)
        self.label2.move(500,40)
        # line 1
        self.line1 = QLineEdit(self)
        self.line1.setFont(font)
        self.line1.move(500,60)
        self.line1.setFixedWidth(400)
        self.line1.setFixedHeight(50)
        
        # label 3
        self.label3 = QLabel(self)
        self.label3.setText("Enter your last name")
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        font3.setCapitalization(True)
        self.label3.setFont(font2)
        self.label3.move(500,130)
        # line 2
        self.line2 = QLineEdit(self)
        self.line2.setFont(font)
        self.line2.move(500,150)
        self.line2.setFixedWidth(400)
        self.line2.setFixedHeight(50)

        # label 4
        self.label3 = QLabel(self)
        self.label3.setText("Enter your email address")
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        font3.setCapitalization(True)
        self.label3.setFont(font2)
        self.label3.move(500,220)
        # line 3
        self.line2 = QLineEdit(self)
        self.line2.setFont(font)
        self.line2.move(500,240)
        self.line2.setFixedWidth(400)
        self.line2.setFixedHeight(50)

        # label 4
        self.label3 = QLabel(self)
        self.label3.setText("Enter your password")
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        font3.setCapitalization(True)
        self.label3.setFont(font2)
        self.label3.move(500,310)
        # line 4
        self.line2 = QLineEdit(self)
        self.line2.setFont(font)
        self.line2.move(500,330)
        self.line2.setFixedWidth(400)
        self.line2.setFixedHeight(50)

        # Qpushbutton
        font4 = QFont()
        font4.setBold(True)
        font4.setCapitalization(True)
        button = QPushButton(self)
        button.setText("Register Now")
        button.move(500,390)
        button.setFixedWidth(150)
        button.setFixedHeight(60)
        button.setFont(font4)

        font4 = QFont()
        font4.setBold(True)
        font4.setCapitalization(True)
        button1 = QPushButton(self)
        button1.setText("I have an account")
        button1.move(750,390)
        button1.setFixedWidth(150)
        button1.setFixedHeight(60)
        button1.setFont(font4)
        # button1.clicked.connect(login.Login())

    # def download_images(self):
    #     search_query = self.line1.text()
    #     num_images = int(self.line2.text())
    #     pi.download(search_query, num_images)

def Register():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    Register()