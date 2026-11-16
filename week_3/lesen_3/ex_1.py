from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Window Title")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Hello, PySide6!", self)
        self.label.setGeometry(30, 30, 300, 30)

        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(30, 80, 200, 30)
        self.name_input.setPlaceholderText("Enter your name")
        self.name_input.textChanged.connect(self.name_changed)

        self.button = QPushButton("Click me", self)
        self.button.setGeometry(30, 130, 120, 40)
        self.button.clicked.connect(self.button_clicked)

    def name_changed(self, text):
        self.label.setText(f"Hello {text}")

    def button_clicked(self):
        self.label.setText("The button was clicked!")

if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()