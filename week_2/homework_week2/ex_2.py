from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

app= QApplication()

window= QWidget()
window.setGeometry(50, 50, 500, 300)
window.setStyleSheet('font-size: 16xp')

output_text=QLabel('', window)
output_text.setGeometry(20, 20, 300, 30)
output_text.setStyleSheet('backgeound-color:lightgray')

in_text= QLineEdit('', window)
in_text.setGeometry(20, 80, 300, 30)

def say_hello():
    name= in_text.text()
    output_text.setText(f'Hello {name}, your name is {len(name)} letters long ')

in_text.returnPressed.connect(say_hello)

window.show()
app.exec()
