import json
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import hashlib

class pos_setting:
    data_file = "Database/addproducts.json"
    add_users = "Database/addusers.json"
    roles_path = "Database/role.json"

    font1 = QFont()
    font1.setBold(True)
    def __init__(self, datafile, add_users, roles_path):
        self.roles_path = roles_path
        
    def addproduct(self,product_name1,product_brand1, product_vat1, product_code1, product_price1,
                    product_quantity1, percentage_vat1):

        # check if database exist
        if not os.path.exists(pos_setting.data_file):
            with open(self.data_file, "w") as f:
                json.dump([], f)

        product_name = product_name1.text().lower()
        product_brand = product_brand1.text().lower()
        product_vat = product_vat1.text().lower()
        product_code = product_code1.text().lower()
        try:
            product_price = int(product_price1.text())
            product_quantity = int(product_quantity1.text())
            percentage_vat = int(percentage_vat1.text())
            print("Product")
            product_total_amount = ((product_price + (percentage_vat/100*product_price))*product_quantity)
        except Exception as e:
            message2 =QMessageBox()
            message2.setFont(pos_setting.font1)
            message2.warning(None, "invalid number",str(e))
        try:
            with open(pos_setting.data_file, "r") as f:
                json_data = json.load(f)
                uniqui_code = [data.get('product code') for data in json_data]
                if product_code in  uniqui_code:
                    message_code = QMessageBox()
                    message_code.warning(None, "code error", "Product Code has been assigned to another product")
                else:
                    try:
                        data = {
                            "product name": product_name,
                            "product quantity": product_quantity,
                            "product price": product_price,
                            "product code": product_code,
                            "product brand": product_brand,
                            "product vat": product_vat,
                            "percentage vat": percentage_vat,
                            "total amount": product_total_amount
                        }
                        json_data.append(data)
                        with open( pos_setting.data_file, 'w') as f:
                            json.dump(json_data, f, indent=2)
                            messd =QMessageBox()
                            messd.setFont(pos_setting.font1)
                            messd.information(None, "saving","Product has been added successfully")

                    except Exception:
                        mess =QMessageBox()
                        mess.setFont(self.font1)
                        mess.warning(None, "Invalid role",str(Exception))
        except Exception:
            message =QMessageBox()
            message.setFont(pos_setting.font1)
            message.warning(None, "not saved", str(Exception))

    def addusers(self, first_name1, last_name1, role1, username1, password1, blood_group1,
                 salary1, national_id1):
        # Check if data file exists, otherwise create an empty file with an empty JSON array
        try:
            if not os.path.exists(pos_setting.add_users):
                with open(pos_setting.add_users, "w") as f:
                    json.dump([], f)
        except Exception as e:
            message1 =QMessageBox()
            message1.setFont(pos_setting.font1)
            message1.warning(None, "Directory",str(e))
        firstName = first_name1.text().lower()
        lastname = last_name1.text().lower()
        role = role1.text().lower()
        username = username1.text().lower()
        password = password1.text().lower()
        bloodgroup = blood_group1.text().lower()
        try:
            salary = int(salary1.text())
            nationalId = int(national_id1.text())
        except Exception as e:
            message2 =QMessageBox()
            message2.setFont(pos_setting.font1)
            message2.warning(None, "invalid number","Salary or your national Identity is not a valid number")
        roles1 = "Database/role.json"

        with open(roles1, "r") as f:
            data = json.load(f)

        roles = [role["role"] for role in data]

        # print(roles)
        # with open(data_file, "r") as f2:
        #     role = json.load(f2)
        #     roles = [role["role"] for role in data]
        #     print(roles)
                
        pawd = hashlib.md5(password.encode()).hexdigest()
        # try:
        with open(pos_setting.add_users, "r") as f:
            json_data = json.load(f)
            usernames = [data.get("username") for data in json_data]
            nat_id = [data1.get("National ID")  for data1 in json_data]
            li = [usernames, nat_id]            
            if username in usernames and nationalId in nat_id:
                mess_username = QMessageBox()
                mess_username.setFont(pos_setting.font1)
                mess_username.warning(None,"Error in username", "Username already taken kindly change your username!!!!")
            else:
                if role in roles:
                    data = {
                        "Firstname": firstName,
                        "lastname": lastname,
                        "role": role,
                        "username": username,
                        "password": pawd,
                        "salary": salary,
                        "National ID": nationalId,
                        "Blood Type": bloodgroup
                    }
                    json_data.append(data)
                    with open(pos_setting.add_users, 'w') as f:
                        json.dump(json_data, f, indent=2)
                        messd =QMessageBox()
                        messd.setFont(pos_setting.font1)
                        messd.information(None, "saving","Your Data has been saved successfully")

                else:
                    mess =QMessageBox()
                    mess.setFont(pos_setting.font1)
                    mess.warning(None, "Invalid role","Role is not available, kindly confirm from administrator")
        # except Exception:
        #     message =QMessageBox()
        #     message.setFont(font1)
        #     message.warning(None, "not saved", str(Exception))

    def roles(self, role1):
        # Check if data file exists, otherwise create an empty file with an empty JSON array
        if not os.path.exists(self.roles_path):
            with open(self.roles_path, "w") as f:
                json.dump([], f)
        role = role1.text().lower()
        try:
            with open(self.roles_path, "r") as f:
                json_data = json.load(f)
                role_saved = [data.get("role") for data in json_data]
                if role in role_saved:
                    m = QMessageBox()
                    m.warning(None, "already exists", "Role already exists in the system")
                else:
                    with open(self.roles_path, 'w') as f:
                        data = {"role": role}
                        json_data.append(data)
                        json.dump(json_data, f, indent=2)
                        messd =QMessageBox()
                        messd.setFont(pos_setting.font1)
                        messd.warning(None, "saving","Role has been saved successfully")
        except Exception:
            message =QMessageBox()
            message.setFont(pos_setting.font1)
            message.warning(None, "not saved", str(Exception))

