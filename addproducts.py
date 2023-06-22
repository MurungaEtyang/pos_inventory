from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import databaseApi.save_data.save_databaseapi as addproducts
class show_Dataset(QDialog):
    def __init__(self , parent=None):
        super(show_Dataset, self).__init__(parent)
        self.setModal(True)
        self.resize(500, 600)
        self.setWindowTitle("add products")
        self.setFixedWidth(600)
        self.adjustSize()
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        # header
        self.label = QLabel(self)
        self.label.setText("Add products")
        self.label.move(260,20)
        self.label.setFont(font)

        # Product name label
        self.label1 = QLabel(self)
        self.label1.setText("Product:")
        self.label1.move(30,70)
        self.label1.setFont(font)
        # Product name
        self.product_name = QLineEdit(self)
        self.product_name.setFont(font)
        self.product_name.move(150,60)
        self.product_name.setFixedWidth(300)
        self.product_name.setFixedHeight(40)

        # Username label
        self.label1 = QLabel(self)
        self.label1.setText("Price:")
        self.label1.move(30,130)
        self.label1.setFont(font)
        # Product price
        self.product_price = QLineEdit(self)
        self.product_price.setFont(font)
        self.product_price.move(150,120)
        self.product_price.setFixedWidth(300)
        self.product_price.setFixedHeight(40)

        # product code label
        self.label1 = QLabel(self)
        self.label1.setText("product codes:")
        self.label1.move(30,190)
        self.label1.setFont(font)
        # product codes
        self.product_code = QLineEdit(self)
        self.product_code.setFont(font)
        self.product_code.move(150,180)
        self.product_code.setFixedWidth(300)
        self.product_code.setFixedHeight(40)

        # product Quantity label
        self.label1 = QLabel(self)
        self.label1.setText("product Quantity:")
        self.label1.move(30,250)
        self.label1.setFont(font)
        # Product Quantity
        self.product_quantity = QLineEdit(self)
        self.product_quantity.setFont(font)
        self.product_quantity.move(150,240)
        self.product_quantity.setFixedWidth(300)
        self.product_quantity.setFixedHeight(40)

        # product brand label
        self.label1 = QLabel(self)
        self.label1.setText("product brand:")
        self.label1.move(30,310)
        self.label1.setFont(font)
        # Procuct brand
        self.product_brand = QLineEdit(self)
        self.product_brand.setFont(font)
        self.product_brand.move(150,300)
        self.product_brand.setFixedWidth(300)
        self.product_brand.setFixedHeight(40)

        # Type of VAT label
        self.label1 = QLabel(self)
        self.label1.setText("VAT type(kra): ")
        self.label1.move(30,370)
        self.label1.setFont(font)
        # VAT 
        self.VAT = QLineEdit(self)
        self.VAT.setFont(font)
        self.VAT.move(150,360)
        self.VAT.setFixedWidth(300)
        self.VAT.setFixedHeight(40)

        # Vat percentage label
        self.label1 = QLabel(self)
        self.label1.setText("Tax %:")
        self.label1.move(30,430)
        self.label1.setFont(font)
        # VAT percentage
        self.VAT_PERCENTAGE = QLineEdit(self)
        self.VAT_PERCENTAGE.setFont(font)
        self.VAT_PERCENTAGE.move(150,420)
        self.VAT_PERCENTAGE.setFixedWidth(300)
        self.VAT_PERCENTAGE.setFixedHeight(40)

        # button
        self.button = QPushButton(self)
        self.button.setFont(font)
        self.button.setFixedWidth(100)
        self.button.setFixedHeight(30)
        self.button.setText("Send Data")
        self.button.move(250, 500)
        self.button.clicked.connect(self.savaData)

        # function for data 
    def savaData(self):
        product_name = self.product_name
        product_brand = self.product_brand
        product_vat = self.VAT
        product_code = self.product_code
        product_price = self.product_price
        product_quantity = self.product_quantity
        addproducts.pos_setting.addproduct(self, product_name, product_brand, product_vat, product_code, product_price, product_quantity, self.VAT_PERCENTAGE)