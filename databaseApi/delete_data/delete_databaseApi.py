from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json

class delete_data:
    font1 = QFont()
    font1.setBold(True)
    users = "Database/addusers.json"
    data_file_role = "Database/role.json"
    data_file_products = "Database/addproducts.json"
    def __init__(self):
        pass

    def delete_users(self, users):
        delete_data.__delete_users__(self, users)
        
    def __delete_users__(self, users):
        input_text = users.text()
        try:
            with open(delete_data.users, "r") as f:
                json_data = json.load(f)
            filtered_data = [item for item in json_data if item['username'] != input_text]

            if len(filtered_data) == len(json_data):
                QMessageBox.warning(self, "Error", f"User '{input_text}' does not exist.")
            else:
                with open(delete_data.users, "w") as f:
                    json.dump(filtered_data, f, indent=4)

                QMessageBox.information(self, "Success", f"User '{input_text}' and its related data have been deleted successfully.")
        except Exception as e:
            QMessageBox.warning(self, "error!", f"User '{input_text}' and its related data has not deleted successfully.")

    def delete_roles(self, roles):
        delete_data.__delete_roles__(self , roles)

    def __delete_roles__(self, roles):
        input_text = roles.text()
        try:
            with open(delete_data.data_file_role, "r") as f:
                json_data = json.load(f)

            filtered_data = [item for item in json_data if item['role'] != input_text]

            if len(filtered_data) == len(json_data):
                QMessageBox.warning(self, "Error", f"Role '{input_text}' does not exist.")
            else:
                with open(delete_data.data_file_role, "w") as f:
                    json.dump(filtered_data, f, indent=4)

                QMessageBox.information(self, "Success", f"Role '{input_text}' and its related data have been deleted successfully.")
        except Exception as e:
            QMessageBox.warning(self, "error!", f"Role '{input_text}' and its related data has not deleted successfully.") 
    
    def delete_products(self , input_text):
        delete_data.__delete_products__(self, input_text)

    def __delete_products__(self, input_text1):
        input_text = input_text1.text()

        try:
            with open(delete_data.data_file_products, "r") as f:
                json_data = json.load(f)

            filtered_data = [item for item in json_data if item['product code'] != input_text and item['product name'] != input_text]

            with open(delete_data.data_file_products, "w") as f:
                json.dump(filtered_data, f, indent=4)

            QMessageBox.information(self, "Success", f"Product '{input_text}' and its related data deleted successfully.")
        except Exception as e:
            print(e)   