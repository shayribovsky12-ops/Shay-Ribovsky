from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton
app = QApplication()
window= QWidget()

window.setWindowTitle('my first program')
window.setGeometry(100, 100, 500, 300) #x, y, w, h
window.setStyleSheet('background-color: yellow')

text = QLabel('This is nice!', window)
text.setGeometry(50, 50, 300, 30)
text.setStyleSheet('background-color: gray; font-siz: 20xp; color:red; font-family: consolas; font-weight: bold')

def butt_fun():
    text.setText('This is super nice!')

button = QPushButton('Click me', window)
button.setGeometry(50, 100, 300, 30)
button.setStyleSheet('font-size: 20xp')
button.clicked.connect(butt_fun)


window.show()
app.exec()