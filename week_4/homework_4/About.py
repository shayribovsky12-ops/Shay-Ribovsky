from PySide6.QtWidgets import QWidget, QLabel


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.about_my()

    def about_my(self):
        self.setWindowTitle("About Me")
        self.setGeometry(150, 150, 560, 260)

        self.name_label = QLabel("Name: shay ribovski", self)
        self.name_label.setGeometry(20, 20, 520, 30)

        self.email_label = QLabel("Email: shay.ribovski@s.afeka.ac.il", self)
        self.email_label.setGeometry(20, 60, 520, 30)

        self.link_label = QLabel(
            '<a href="https://www.linkedin.com/">LinkedIn</a>', self
        )
        self.link_label.setOpenExternalLinks(True)
        self.link_label.setGeometry(20, 100, 520, 30)

        self.github_label = QLabel(
            'GitHub: <a href="https://github.com/shayribovsky12-ops/Shay-Ribovsky">'
            'https://github.com/shayribovsky12-ops/Shay-Ribovsky</a>',
            self,
        )
        self.github_label.setOpenExternalLinks(True)
        self.github_label.setGeometry(20, 140, 520, 30)
