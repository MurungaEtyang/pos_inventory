from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import databaseApi.save_data.save_databaseapi as users
class show_Dataset(QDialog):
    def __init__(self , parent=None):
        super(show_Dataset, self).__init__(parent)
        self.setModal(True)
        self.resize(800, 600)
        self.setWindowTitle("Add new dataset")
        self.setFixedWidth(600)
        self.adjustSize()
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        # header
        self.label = QLabel(self)
        self.label.setText("Save users to the database")
        self.label.move(260,20)
        self.label.setFont(font)
        # First name label
        self.label1 = QLabel(self)
        self.label1.setText("First name:")
        self.label1.move(60,63)
        self.label1.setFont(font)
        # first Name input
        self.first_name = QLineEdit(self)
        self.first_name.setFont(font)
        self.first_name.move(150,50)
        self.first_name.setFixedHeight(40)
        self.first_name.setFixedWidth(300)

        # Last name label
        self.label1 = QLabel(self)
        self.label1.setText("last name:")
        self.label1.move(60,113)
        self.label1.setFont(font)
        # last name input
        self.last_name = QLineEdit(self)
        self.last_name.setFont(font)
        self.last_name.move(150,100)
        self.last_name.setFixedWidth(300)
        self.last_name.setFixedHeight(40)


        # Role label
        self.label1 = QLabel(self)
        self.label1.setText("Role:")
        self.label1.move(60,163)
        self.label1.setFont(font)
        # Role selection
        self.role = QLineEdit(self)
        self.role.setFont(font)
        self.role.move(150,150)
        self.role.setFixedWidth(300)
        self.role.setFixedHeight(40)

        # Username label
        self.label1 = QLabel(self)
        self.label1.setText("Username:")
        self.label1.move(60,213)
        self.label1.setFont(font)
        # username
        self.username = QLineEdit(self)
        self.username.setFont(font)
        self.username.move(150,200)
        self.username.setFixedWidth(300)
        self.username.setFixedHeight(40)

        # Password label
        self.label1 = QLabel(self)
        self.label1.setText("Password:")
        self.label1.move(60,263)
        self.label1.setFont(font)
        # password
        self.password = QLineEdit(self)
        self.password.setFont(font)
        self.password.move(150,250)
        self.password.setFixedWidth(300)
        self.password.setFixedHeight(40)
        self.password.setEchoMode(QLineEdit.Password)
        
        # salary
        self.label1 = QLabel(self)
        self.label1.setText("SALARY: ")
        self.label1.move(60,313)
        self.label1.setFont(font)
        # Salary
        self.salary = QLineEdit(self)
        self.salary.setFont(font)
        self.salary.move(150,300)
        self.salary.setFixedWidth(300)
        self.salary.setFixedHeight(40)

        # salary
        self.label1 = QLabel(self)
        self.label1.setText("National ID: ")
        self.label1.move(60,363)
        self.label1.setFont(font)
        # Salary
        self.national_id = QLineEdit(self)
        self.national_id.setFont(font)
        self.national_id.move(150,350)
        self.national_id.setFixedWidth(300)
        self.national_id.setFixedHeight(40)

        # blood group
        self.label1 = QLabel(self)
        self.label1.setText("blood group: ")
        self.label1.move(60,413)
        self.label1.setFont(font)
        # blood group
        self.blood_group = QLineEdit(self)
        self.blood_group.setFont(font)
        self.blood_group.move(150,400)
        self.blood_group.setFixedWidth(300)
        self.blood_group.setFixedHeight(40)

        # button
        self.button = QPushButton(self)
        self.button.setFont(font)
        self.button.setFixedWidth(100)
        self.button.setFixedHeight(50)
        self.button.setText("Send Data")
        self.button.move(250, 470)
        self.button.clicked.connect(self.savaData)

        # function for data 
    def savaData(self):
        firstName = self.first_name
        lastname = self.last_name
        role = self.role
        username = self.username
        password = self.password
        bloodgroup = self.blood_group
        salary = self.salary
        nationalId = self.national_id
        
        users.pos_setting.addusers(self, firstName, lastname, role, username, password, salary, nationalId, bloodgroup)