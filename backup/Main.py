import socket
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMessageBox
import login, pyqt5

def check_internet_connection():
    try:
        socket.create_connection(("www.kenflix.xyz", 80))
        return True
    except OSError:
        return False

app = QApplication([])

def check_connection():
    message = QMessageBox()
    message.setMinimumHeight(500)
    message.setMinimumHeight(500)
    message.setWindowFlags(Qt.WindowStaysOnTopHint)
    if check_internet_connection():
        login.Login()
    else:
        message.warning(None, "Connection Status", "No internet connection! Kindly connect internet to proceed")

# Check connection status every 5 seconds
timer = QTimer()
timer.timeout.connect(check_connection)
timer.start(2000)

app.exec()
