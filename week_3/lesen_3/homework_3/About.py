from PySide6.QtWidgets import QWidget, QLabel

class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.about_my()

    def about_my(self):
        self.setWindowTitle("About Me")
        self.setGeometry(150, 150, 450, 500)
        self.setStyleSheet("background-color: lightblue;")

        self.name_label = QLabel("Name: shay ribovski", self)
        self.name_label.setGeometry(20, 20, 250, 30)

        self.email_label = QLabel("Email: shay.ribovski@s.afeka.ac.il", self)
        self.email_label.setGeometry(20, 60, 250, 30)

        self.link_label = QLabel('<a href="https://www.linkedin.com/">LinkedIn</a>', self)
        self.link_label.setOpenExternalLinks(True)
        self.link_label.setGeometry(20, 100, 250, 30)

        image_bank = '<img src="bank_image.jpg" width="400" height="300">'
        
        self.image_label = QLabel(image_bank, self)
        self.image_label.setGeometry(20, 140, 400, 300)