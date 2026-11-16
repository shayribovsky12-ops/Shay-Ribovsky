from PySide6.QtWidgets import QApplication, QWidget, QDoubleSpinBox, QSpinBox

app= QApplication() 
window= QWidget()
window.setGeometry(50, 50, 600, 300)
window.setStyleSheet('font-size:16px')

number1 = QSpinBox(window)
number1.setGeometry(30, 30, 200, 30)
number1.setRange(-10, 10)

number2 = QSpinBox(window)
number2.setGeometry(30, 80, 200, 30)
number2.setRange(0, 100)
number2.setReadOnly(True)

def squr_num():
    value= number1.value()
    number2.setValue(value ** 2)
number1.editingFinished.connect(squr_num)

window.show()
app.exec()