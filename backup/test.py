import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class ImageGallery(QMainWindow):
    def __init__(self, image_folder):
        super().__init__()

        self.image_folder = image_folder
        self.image_labels = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Image Gallery")

        scroll_area = QScrollArea()
        main_widget = QWidget()
        layout = QGridLayout()
        main_widget.setLayout(layout)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(main_widget)
        self.setCentralWidget(scroll_area)

        self.update_gallery()

    def update_gallery(self):
        layout = self.centralWidget().widget().layout()
        if layout:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().setParent(None)

        image_files = os.listdir(self.image_folder)

        available_width = self.centralWidget().widget().width()

        num_columns = max(1, available_width // 200)  # Each image has a width of 200 pixels
        num_rows = (len(image_files) + num_columns - 1) // num_columns

        for file in image_files:
            if file.endswith(".jpg") or file.endswith(".png"):
                image_path = os.path.join(self.image_folder, file)
                pixmap = QPixmap(image_path)

                width = available_width // num_columns - 10  # Subtracting 10 for margin
                height = width * pixmap.height() // pixmap.width()

                label = QLabel()
                label.setPixmap(pixmap.scaled(width, height, Qt.KeepAspectRatio))
                layout.addWidget(label)

        self.centralWidget().widget().setLayout(layout)

    def resizeEvent(self, event):
        self.update_gallery()
        return super().resizeEvent(event)


if __name__ == "__main__":
    app = QApplication([])
    folder_path = "images/Ruto"  # Replace with your image folder path
    window = ImageGallery(folder_path)
    window.show()
    app.exec_()
