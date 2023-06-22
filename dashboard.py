from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 

import addproducts, addusers, roles, delete_product, delete_role, delete_users

class show_Dataset(QWidget):
    def __init__(self , parent=None):
        super(show_Dataset, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("administrative dashboard")
        self.isFullScreen()
        self.adjustSize()
        
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        # header
        self.label = QLabel(self)
        self.label.setText("Welcome to administrative dashboard")
        self.label.move(500,20)
        self.label.setFont(font)
        self.label.setFixedHeight(70)
        # button0
        self.button0 = QPushButton(self)
        self.button0.setFont(font)
        self.button0.setFixedWidth(200)
        self.button0.setFixedHeight(50)
        self.button0.setText("ADD ROLES")
        self.button0.move(10, 100)
        self.button0.setStyleSheet("background-color: rgb(100,149,237)")
        self.button0.clicked.connect(self.launch_role_file)

        # button1
        self.button1 = QPushButton(self)
        self.button1.setFont(font)
        self.button1.setFixedWidth(200)
        self.button1.setFixedHeight(50)
        self.button1.setText("ADD USERS")
        self.button1.move(220, 100)
        self.button1.setStyleSheet("background-color: rgb(100,149,237)")
        self.button1.clicked.connect(self.launch_adduser_file)

        # button2
        self.button2 = QPushButton(self)
        self.button2.setFont(font)
        self.button2.setFixedWidth(200)
        self.button2.setFixedHeight(50)
        self.button2.setText("Add Products")
        self.button2.move(430, 100)
        self.button2.setStyleSheet("background-color: rgb(100,149,237)")
        self.button2.clicked.connect(self.launch_addproducts_file)

        # button3
        self.button3 = QPushButton(self)
        self.button3.setFont(font)
        self.button3.setFixedWidth(200)
        self.button3.setFixedHeight(50)
        self.button3.setText("delete products")
        self.button3.move(640, 100)
        self.button3.setStyleSheet("background-color: rgb(100,149,237)")
        self.button3.clicked.connect(self.launch_deleteproducts_file)

        # button4
        self.button4 = QPushButton(self)
        self.button4.setFont(font)
        self.button4.setFixedWidth(200)
        self.button4.setFixedHeight(50)
        self.button4.setText("delete users")
        self.button4.move(850, 100)
        self.button4.setStyleSheet("background-color: rgb(100,149,237)")
        self.button4.clicked.connect(self.launch_deleteusers_file)

        # button5
        self.button5 = QPushButton(self)
        self.button5.setFont(font)
        self.button5.setFixedWidth(200)
        self.button5.setFixedHeight(50)
        self.button5.setText("Delete roles")
        self.button5.move(1060, 100)
        self.button5.setStyleSheet("background-color: rgb(100,149,237)")
        self.button5.clicked.connect(self.launch_deleterole_file)

    def launch_role_file(self):
        self.roles = roles.show_Dataset()
        self.roles.show()

    def launch_adduser_file(self):
        self.addusers = addusers.show_Dataset()
        self.addusers.show()

    def launch_addproducts_file(self):
        self.addproducts = addproducts.show_Dataset()
        self.addproducts.show()

    def launch_deleteproducts_file(self):
        self.deleteproducts = delete_product.show_Dataset()
        self.deleteproducts.show()

    def launch_deleteusers_file(self):
        self.deleteusers = delete_users.show_Dataset()
        self.deleteusers.show()

    def launch_deleterole_file(self):
        self.deleterole = delete_role.show_Dataset()
        self.deleterole.show()
 
        
def main():
    app = QApplication(sys.argv)
    app1 = show_Dataset()
    app1.showMaximized()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
        