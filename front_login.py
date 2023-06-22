from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import dashboard
import hashlib, time_day, pos_sale
import time
import json
import sys


class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.resize(500,400)
        self.setWindowTitle("Login")
        # self.setFixedWidth(600)
        self.adjustSize()
        # label 1 (header)
        self.label = QLabel(self)
        self.label.setText("Welcome to Login page") 
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setCapitalization(True)
        self.label.setFont(font)
        self.label.move(180,20)
        
        # label 2
        self.label2 = QLabel(self)
        self.label2.setText("Enter your username")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(True)
        font2.setCapitalization(True)
        self.label2.setFont(font2)
        self.label2.move(120,60)
        # line 1
        self.username = QLineEdit(self)
        self.username.setFont(font)
        self.username.move(120,90)
        self.username.setFixedWidth(400)
        self.username.setFixedHeight(50)
        self.username.setFont(font)
        self.username.setStyleSheet("Background-color: white")
        
        # label 3
        self.label3 = QLabel(self)
        self.label3.setText("Enter your password")
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        font3.setCapitalization(True)
        self.label3.setFont(font2)
        self.label3.move(120,160)
        self.username.setStyleSheet("Background-color: white")

        # line 2
        self.password = QLineEdit(self)
        self.password.setFont(font)
        self.password.move(120,180)
        self.password.setFixedWidth(400)
        self.password.setFixedHeight(50)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFont(font)
        self.password.setStyleSheet("Background-color: white")

        # Qpushbutton
        font4 = QFont()
        font4.setBold(True)
        font4.setCapitalization(True)
        button = QPushButton(self)
        button.setText("Login")
        button.move(250, 260)
        button.setFixedWidth(150)
        button.setFixedHeight(60)
        button.setFont(font4)
        button.setStyleSheet("Background-color: white")
        button.clicked.connect(self.self_login)


    def day_time(self):
        font = QFont()
        font.setCapitalization(True)
        font.setBold(True)
        font.setPointSize(20)
        self.label1 = QLabel(self)
        self.label1.setText(time_day.a) 
        self.label1.setStyleSheet("background-color: white; color:black")
        self.label1.setFont(font)
        self.label1.move(10,350)

        self.label1 = QLabel(self)
        self.label1.setText(time.ctime()) 
        self.label1.setStyleSheet("background-color: white; color:black;")
        self.label1.setFont(font)
        self.label1.move(10,400)
  
        # A--------------Z
                # A
    def alphabets(self, letters, target_input):
        lettersfont4 = QFont()
        lettersfont4.setBold(True)
        lettersfont4.setCapitalization(True)
        lettersfont4.setPixelSize(16)
        A = QPushButton(self)
        A.setFixedWidth(100)
        A.setFixedHeight(60)
        A.setStyleSheet(
                "background-color: rgb(236,133,253)"
                )     
        A.setFont(lettersfont4)
        A.setText(letters)
        A.clicked.connect(lambda checked, value=letters, target=target_input: self.handle_button_click(value, target))  # Connect button to a function

        return A

    def handle_button_click(self, letter, target):

        if target == self.username:
            self.username.setText(self.username.text() + letter)
        else:
            self.password.setText(self.password.text() + letter)

    def create_buttons(self):
        l = dict(a=600, b=700, c=800, d=900, e=1000, f=1100, g=1200)
        for k, v in l.items():
            self.alphabets(k, self.username).move(v, 20)

        l = dict(h=600, i=700, j=800, k=900, l=1000, m=1100, n=1200)
        for k, v in l.items():
            self.alphabets(k, self.username).move(v, 80)

        l = dict(o=600, p=700, q=800, r=900, s=1000, t=1100, u=1200)
        for k, v in l.items():
            self.alphabets(k, self.username).move(v, 140)

        l = dict(v=600, w=700, x=800, y=900, z=1000)
        for k, v in l.items():
            self.alphabets(k, self.username).move(v, 200)

        n = {'1': 800, '2': 900, '3': 1000}
        for k, v in n.items():
            self.alphabets(k, self.username).move(v, 300)

        n = {'4': 800, '5': 900, '6': 1000}
        for k, v in n.items():
            self.alphabets(k, self.username).move(v, 360)

        n = {'7': 800, '8': 900, '9': 1000}
        for k, v in n.items():
            self.alphabets(k, self.username).move(v, 420)

        n = {'0': 900}
        for k, v in n.items():
            self.alphabets(k, self.username).move(v, 480)

        n = {'delete': 800, 'clear': 1000}
        for k, v in n.items():
            self.alphabets(k, self.username).move(v, 480)
        
        
    def self_login(self):
        username = self.username.text()
        p = self.password.text()
        password = hashlib.md5(p.encode()).hexdigest()
        data_json = "Database/addusers.json"
        with open(data_json, "r") as f:
            data1 = json.load(f)

            user_name = [data.get('username') for data in data1]
            passwd = [data.get('password') for data in data1]
            if username in user_name and password in passwd:
                if username == "admin":
                    self.open_dashboard()
                
                else:
                    self.pos_dashboard()
            else:
                messd1 =QMessageBox()
                messd1.warning(None, "warning","Wrong username or password")

    def open_dashboard(self):
        self.dashboard = dashboard.show_Dataset()
        self.dashboard.showMaximized()
        self.dashboard.show()
    def pos_dashboard(self):
        self.pos_sale = pos_sale.show_Dataset()
        self.pos_sale.showFullScreen()
        self.pos_sale.show()

def Login():
    app = QApplication(sys.argv)
    ex = window()
    ex.create_buttons()
    ex.day_time()
    ex.showMaximized()
    ex.setStyleSheet("background-color: rgb(176,164,178))")
    ex.show()
    app.exec_()

if __name__ == '__main__':
    Login()
