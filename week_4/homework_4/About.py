from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.about_me()

    def about_me(self):
        self.setWindowTitle("About Me")
        self.setGeometry(200, 200, 420, 280)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        self.title_label = QLabel("About Me")
        self.title_label.setObjectName("aboutTitle")

        self.name_label = QLabel("Name: Shay Ribovski")
        self.name_label.setObjectName("aboutInfo")

        self.email_label = QLabel("Email: shay.ribovski@s.afeka.ac.il")
        self.email_label.setObjectName("aboutInfo")

        self.linkedin_label = QLabel(
            'LinkedIn: <a href="https://www.linkedin.com/">LinkedIn Profile</a>'
        )
        self.linkedin_label.setObjectName("aboutInfo")
        self.linkedin_label.setOpenExternalLinks(True)

        self.github_label = QLabel(
            'GitHub Repository: <a href="https://github.com/YOUR_USERNAME/YOUR_REPO">'
            'https://github.com/YOUR_USERNAME/YOUR_REPO</a>'
        )
        self.github_label.setObjectName("aboutInfo")
        self.github_label.setOpenExternalLinks(True)

        layout.addWidget(self.title_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.email_label)
        layout.addWidget(self.linkedin_label)
        layout.addWidget(self.github_label)
        layout.addStretch()

        self.setLayout(layout)
