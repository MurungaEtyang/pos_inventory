from pygoogle_image import image as pi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class DownloaderThread(QThread):
    progress_updated = pyqtSignal(int)

    def __init__(self, search_query, num_images):
        super().__init__()
        self.search_query = search_query
        self.num_images = num_images

    def run(self):
        self.progress_updated.emit(0)  # Initial value
        pi.download(self.search_query, self.num_images, self.update_progress)
        self.progress_updated.emit(100)  # Finished value

    def update_progress(self, progress):
        self.progress_updated.emit(progress)

class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        # self.resize(200,50)
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

        # QProgressBar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, 220, 380, 20)

        # Qpushbutton
        font4 = QFont()
        font4.setBold(True)
        font4.setCapitalization(True)
        button = QPushButton(self)
        button.setText("Download now...")
        button.move(120, 250)
        button.setFixedWidth(150)
        button.setFixedHeight(60)
        button.setFont(font4)
        button.clicked.connect(self.download_images)

    def download_images(self):
        search_query = self.line1.text()
        num_images = int(self.line2.text())

        self.downloader_thread = DownloaderThread(search_query, num_images)
        self.downloader_thread.progress_updated.connect(self.update_progress)
        self.downloader_thread.start()

    def update_progress(self, progress):
        self.progress_bar.setValue(progress)

def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
