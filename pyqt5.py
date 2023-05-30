from pygoogle_image import image as pi
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os

class DownloaderThread(QThread):
    images_downloaded = pyqtSignal(list)

    def __init__(self, search_query, num_images):
        super().__init__()
        self.search_query = search_query
        self.num_images = num_images

    def run(self):
        downloaded_images = pi.download(self.search_query, self.num_images)
        self.images_downloaded.emit(downloaded_images)

class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.resize(500,300)
        self.setWindowTitle("pyqt")
        # label 1 (header)
        self.label = QLabel(self)
        self.label.setText("Welcome to image downloader.") 
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.move(50,10)

        # label 2
        self.label2 = QLabel(self)
        self.label2.setText("Enter what you want to download below")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(True)
        font2.setCapitalization(True)
        self.label2.setFont(font2)
        self.label2.move(10,40)
        # line 1
        self.line1 = QLineEdit(self)
        self.line1.setFont(font)
        self.line1.move(10,60)
        self.line1.setFixedWidth(400)
        self.line1.setFixedHeight(50)
        
        # label 3
        self.label3 = QLabel(self)
        self.label3.setText("Enter the number of images to download")
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        font3.setCapitalization(True)
        self.label3.setFont(font2)
        self.label3.move(10,130)
        # line 2
        self.line2 = QLineEdit(self)
        self.line2.setFont(font)
        self.line2.move(10,150)
        self.line2.setFixedWidth(400)
        self.line2.setFixedHeight(50)

        
        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 220, 380, 280)

        # Qpushbutton
        font4 = QFont()
        font4.setBold(True)
        font4.setCapitalization(True)
        button = QPushButton(self)
        button.setText("Download now...")
        button.move(120,220)
        button.setFixedWidth(150)
        button.setFixedHeight(60)
        button.setFont(font4)
        button.clicked.connect(self.download_images)

    def download_images(self):
        search_query = self.line1.text()
        try:
            num_images = int(self.line2.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer for the number of images.")
            return

        self.downloader_thread = DownloaderThread(search_query, num_images)
        self.downloader_thread.images_downloaded.connect(self.display_images)  # Connect images_downloaded signal
        
        self.downloader_thread.start()

    def display_images(self, downloaded_images):
    # Clear existing image
        self.image_label.clear()

        if downloaded_images:
            # Display the first downloaded image
            first_image_path = downloaded_images[0]  # Assuming the first image path is the first element in the list
            pixmap = QPixmap(first_image_path)
            self.image_label.setPixmap(pixmap.scaled(380, 280, Qt.AspectRatioMode.KeepAspectRatio))
        else:
            QMessageBox.warning(self, "No Images", "No images were downloaded.")

        # You can loop through `downloaded_images` to display all the downloaded images if needed



def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()