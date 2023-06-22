from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import databaseApi.save_data.save_databaseapi as roles
class show_Dataset(QDialog):
    roles_path = "Database/role.json"
    def __init__(self , parent=None):
        super(show_Dataset, self).__init__(parent)
        self.setModal(True)
        self.resize(500, 600)
        self.setWindowTitle("Role dataset")
        self.setFixedHeight(300)
        self.setFixedWidth(600)
        self.adjustSize()
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        # header
        self.label = QLabel(self)
        self.label.setText("ADD ROLES")
        self.label.move(260,20)
        self.label.setFont(font)

        self.label1 = QLabel(self)
        self.label1.setText("Role:")
        self.label1.move(110,73)
        self.label1.setFont(font)

        # Role selection
        self.role = QLineEdit(self)
        self.role.setFont(font)
        self.role.move(150,60)
        self.role.setFixedWidth(300)
        self.role.setFixedHeight(40)
        

        # button
        self.button = QPushButton(self)
        self.button.setFont(font)
        self.button.setFixedWidth(100)
        self.button.setFixedHeight(30)
        self.button.setText("Send Data")
        self.button.move(250, 150)
        self.button.clicked.connect(self.savaData)

        # function for data 
    def savaData(self):
        roles.pos_setting.roles(self, self.role)