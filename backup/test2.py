from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import hashlib
import json
import sys
import subprocess
import dashboard

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(500, 400)
        self.setWindowTitle("Login")

        # Create widgets
        self.label = QLabel("Welcome to the Login page", self)
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)

        self.username_label = QLabel("Enter your username", self)
        self.username_edit = QLineEdit(self)

        self.password_label = QLabel("Enter your password", self)
        self.password_edit = QLineEdit(self)
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        hashed_password = hashlib.md5(password.encode()).hexdigest()

        data_json = "Database/addusers.json"
        with open(data_json, "r") as f:
            data1 = json.load(f)
            user_credentials = [(data.get('username'), data.get('password')) for data in data1]

        if (username, hashed_password) in user_credentials:
            QMessageBox.information(self, "Success", "Login successful!")
            self.open_dashboard()
        else:
            QMessageBox.warning(self, "Error", "Wrong username or password!")

    def open_dashboard(self):
        self.dashboard = dashboard.show_Dataset()
        self.dashboard.show()
        self.close()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
