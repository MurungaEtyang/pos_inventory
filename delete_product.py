from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import databaseApi.delete_data.delete_databaseApi as del_products
class show_Dataset(QDialog):
    def __init__(self , parent=None):
        super(show_Dataset, self).__init__(parent)
        self.setModal(True)
        self.resize(500, 600)
        self.setWindowTitle("Delete products")
        self.setFixedHeight(300)
        self.setFixedWidth(600)
        self.adjustSize()
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        # header
        self.label = QLabel(self)
        self.label.setText("delete products")
        self.label.move(260,20)
        self.label.setFont(font)

        self.label1 = QLabel(self)
        self.label1.setText("product code or\n product name:")
        self.label1.move(50,73)
        self.label1.setFont(font)

        # Role selection
        self.role1 = QLineEdit(self)
        self.role1.setFont(font)
        self.role1.move(170,65)
        self.role1.setFixedWidth(300)
        self.role1.setFixedHeight(40)

        # button
        self.button = QPushButton(self)
        self.button.setFont(font)
        self.button.setFixedWidth(100)
        self.button.setFixedHeight(30)
        self.button.setText("Delete")
        self.button.move(250, 150)
        self.button.clicked.connect(self.savaData)

        # function for data 
    def savaData(self):
        del_products.delete_data.delete_products(self, self.role1)
        