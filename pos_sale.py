from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 
import time, time_day, front_login
import json
import os
class show_Dataset(QWidget):
    def __init__(self , parent=None):
        super(show_Dataset, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("POINT OF SALE")
        self.adjustSize()
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        font.setPointSize(13)
        # header
        self.label = QLabel(self)
        self.label.setText("POINT OF SALE")
        self.label.move(800,10)
        self.label.setFont(font)

        self.label = QLabel(self)
        self.label.setText(time.ctime())
        self.label.move(250,10)
        self.label.setFont(font)

        self.logout = QPushButton(self)
        self.logout.setText("logout")
        self.logout.move(1200,10) 
        self.logout.setFont(font)
        self.logout.setFixedHeight(40)
        self.logout.setFixedWidth(150)
        self.logout.clicked.connect(self.open_login)   

        self.label = QLabel(self)
        self.label.setText(time_day.a)
        self.label.move(10,10)
        self.label.setFont(font)

        # SEARCH
        self.search = QLineEdit(self)
        self.search.setPlaceholderText("name of the product or product code")
        self.search.setFont(font)
        self.search.move(30,60)
        self.search.setFixedHeight(50)
        self.search.setFixedWidth(450)
        self.search.setStyleSheet("background-color: #FFFFFF; color:black; border-color:pink; border-radius: 5px;")

        self.search = QLineEdit(self)
        self.search.setPlaceholderText("paid amount")
        self.search.setFont(font)
        self.search.move(30,400)
        self.search.setFixedHeight(50)
        self.search.setFixedWidth(150)
        self.search.setStyleSheet("background-color: rgb(65,74,76)); color:green; border-color:pink; border-radius: 5px;")

        self.search = QLabel(self)
        self.search.setText("paid amount")
        self.search.setFont(font)
        self.search.move(30,320)
        self.search.setFixedHeight(50)
        self.search.setFixedWidth(150)
        self.search.setStyleSheet("background-color: rgb(75,0,130);")

        self.search = QLabel(self)
        self.search.setText("change")
        self.search.setFont(font)
        self.search.move(200,320)
        self.search.setFixedHeight(50)
        self.search.setFixedWidth(150)
        self.search.setStyleSheet("background-color: rgb(75,0,130);")



    def open_login(self):
        self.login = front_login.window()
        self.login.create_buttons()
        self.login.day_time()
        self.login.showMaximized()
        self.login.show()
    def database_reader(self):
        data = "Database/addproducts.json"
        with open(data, "r") as f:
            data_dumps = json.load(f)
            print(data_dumps)
    
        
def main():
    app1 = QApplication(sys.argv)
    app = show_Dataset()
    app.showMaximized()
    # app.showFullScreen()
    app.show()
    sys.exit(app1.exec())
if __name__ == "__main__":
    main()
        