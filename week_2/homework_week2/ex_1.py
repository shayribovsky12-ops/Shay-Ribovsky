from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

app = QApplication()
window = QWidget()
window.setGeometry(50, 50, 400, 300)
window.setStyleSheet("font-size:16px")

text = QLabel("number of clicks : 0", window)
text.setGeometry(50, 50, 300, 30)

text1 = QLabel("", window)
text1.setGeometry(50, 150, 300, 30)
click_count = 0

def butt_fun():
    global click_count
    click_count += 1
    text.setText(f"number of clicks : {click_count}")

def text_fun():
    if click_count % 2 == 0:
        text1.setText("the number is even")
    else:
        text1.setText("")

button = QPushButton("Click me", window)
button.setGeometry(50, 100, 300, 30)
button.setStyleSheet("font-size: 20px")
button.clicked.connect(butt_fun)
button.clicked.connect(text_fun)

window.show()
app.exec()