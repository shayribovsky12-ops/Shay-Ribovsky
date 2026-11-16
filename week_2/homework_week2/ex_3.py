from PySide6.QtWidgets import QApplication, QWidget, QDoubleSpinBox ,QPushButton, QLabel

app= QApplication() 
window= QWidget()
window.setGeometry(50, 50, 600, 300)
window.setStyleSheet('font-size:16px')

button_p = QPushButton('+', window)
button_p.setGeometry(230, 20, 30, 30)
button_p.setStyleSheet('font-size: 20px')

button_mi = QPushButton('-', window)
button_mi.setGeometry(230, 50, 30, 30)
button_mi.setStyleSheet('font-size: 20px')

button_d = QPushButton('*', window)
button_d.setGeometry(230, 80, 30, 30)
button_d.setStyleSheet('font-size: 20px')

button_mu = QPushButton('/', window)
button_mu.setGeometry(230, 110, 30, 30)
button_mu.setStyleSheet('font-size: 20px')

number1 = QDoubleSpinBox(window)
number1.setGeometry(30, 30, 200, 30)
number1.setRange(-100, 100)

number2 = QDoubleSpinBox(window)
number2.setGeometry(30, 80, 200, 30)
number2.setRange(-100, 100)

number3 = QLabel(window)
number3.setGeometry(280,50, 100, 30)
number3.setStyleSheet('background-color: lightgray')
number3.setText("Result")

def sam_num():
    value1= number1.value()
    value2= number2.value()
    number3.setText(str(value1 + value2))
def min_num():
    value1= number1.value()
    value2= number2.value()
    number3.setText(str(value1 - value2))
def mul_num():
    value1= number1.value()
    value2= number2.value()
    number3.setText(str(value1 * value2))
def div_num():
    value1= number1.value()
    value2= number2.value()
    if value2 != 0:
        number3.setText(str(value1 / value2))
    else:
        number3.setText("error")

button_p.clicked.connect(sam_num)
button_mi.clicked.connect(min_num)
button_d.clicked.connect(mul_num)
button_mu.clicked.connect(div_num)

window.show()
app.exec()