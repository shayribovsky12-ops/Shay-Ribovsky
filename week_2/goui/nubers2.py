from PySide6.QtWidgets import QApplication, QWidget, QDoubleSpinBox, QSpinBox ,QPushButton

app= QApplication() 
window= QWidget()
window.setGeometry(50, 50, 600, 300)
window.setStyleSheet('font-size:16px')

button_p = QPushButton('+', window)
button_p.setGeometry(230, 50, 30, 30)
button_p.setStyleSheet('font-size: 20px')

button_m = QPushButton('-', window)
button_m.setGeometry(230, 80, 30, 30)
button_m.setStyleSheet('font-size: 20px')

number1 = QDoubleSpinBox(window)
number1.setGeometry(30, 30, 200, 30)
number1.setRange(-100, 100)

number2 = QDoubleSpinBox(window)
number2.setGeometry(30, 80, 200, 30)
number2.setRange(-100, 100)

number3 = QDoubleSpinBox(window)
number3.setGeometry(260,50, 200, 30)
number3.setRange(-10000, 10000)
number3.setReadOnly(True)

def sam_num():
    value1= number1.value()
    value2= number2.value()
    number3.setValue(value1 + value2)
def min_num():
    value1= number1.value()
    value2= number2.value()
    number3.setValue(value1 - value2)


button_p.clicked.connect(sam_num)

button_m.clicked.connect(min_num)



window.show()
app.exec()