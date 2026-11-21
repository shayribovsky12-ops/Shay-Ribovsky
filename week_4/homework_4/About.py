from PySide6.QtWidgets import QWidget, QLabel


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.about_my()

    def about_my(self):
        self.setWindowTitle("About Me")
        self.setGeometry(150, 150, 450, 260)

        self.name_label = QLabel("Name: shay ribovski", self)
        self.name_label.setGeometry(20, 20, 400, 30)

        self.email_label = QLabel("Email: shay.ribovski@s.afeka.ac.il", self)
        self.email_label.setGeometry(20, 60, 400, 30)

        self.link_label = QLabel(
            '<a href="https://www.linkedin.com/">LinkedIn</a>', self
        )
        self.link_label.setOpenExternalLinks(True)
        self.link_label.setGeometry(20, 100, 400, 30)

        self.github_label = QLabel(
            'GitHub: <a href="https://github.com/YOUR_USERNAME/YOUR_REPO">'
            'https://github.comhttps://github.com/shayribovsky12-ops/Shay-Ribovsky.git</a>',
            self,
        )
        self.github_label.setOpenExternalLinks(True)
        self.github_label.setGeometry(20, 140, 400, 30)
