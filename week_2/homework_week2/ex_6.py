from PySide6.QtWidgets import QApplication, QWidget, QDoubleSpinBox, QPushButton

app = QApplication()
window = QWidget()
window.setGeometry(50, 50, 500, 300)
window.setStyleSheet('font-size:16px')

display = QDoubleSpinBox(window)
display.setGeometry(30, 30, 260, 40)
display.setStyleSheet('font-size: 20px')
display.setRange(-10000, 10000)

button_p = QPushButton('+', window)
button_p.setGeometry(30, 90, 50, 50)
button_p.setStyleSheet('font-size: 20px')

button_mi = QPushButton('-', window)
button_mi.setGeometry(100, 90, 50, 50)
button_mi.setStyleSheet('font-size: 20px')

button_mul = QPushButton('*', window)
button_mul.setGeometry(170, 90, 50, 50)
button_mul.setStyleSheet('font-size: 20px')

button_div = QPushButton('/', window)
button_div.setGeometry(240, 90, 50, 50)
button_div.setStyleSheet('font-size: 20px')

button_eq = QPushButton('=', window)
button_eq.setGeometry(30, 160, 120, 50)
button_eq.setStyleSheet('font-size: 20px')

button_cls = QPushButton('CLS', window)
button_cls.setGeometry(170, 160, 120, 50)
button_cls.setStyleSheet('font-size: 20px')

first_number = 0.0
current_operator = ""

def set_op_add():
    global first_number, current_operator
    first_number = display.value()
    current_operator = "+"
    display.setValue(0) 

def set_op_sub():
    global first_number, current_operator
    first_number = display.value()
    current_operator = "-"
    display.setValue(0)

def set_op_mul():
    global first_number, current_operator
    first_number = display.value()
    current_operator = "*"
    display.setValue(0)

def set_op_div():
    global first_number, current_operator
    first_number = display.value()
    current_operator = "/"
    display.setValue(0)

def calculate():
    global first_number, current_operator
    second_number = display.value()
    
    if current_operator == "+":
        display.setValue(first_number + second_number)
    elif current_operator == "-":
        display.setValue(first_number - second_number)
    elif current_operator == "*":
        display.setValue(first_number * second_number)
    elif current_operator == "/":
        if second_number != 0:
            display.setValue(first_number / second_number)
        else:
            display.setValue(0)  

    current_operator = ""

def clear_screen():
    global first_number, current_operator
    display.setValue(0)
    first_number = 0.0
    current_operator = ""


button_p.clicked.connect(set_op_add)
button_mi.clicked.connect(set_op_sub)
button_mul.clicked.connect(set_op_mul)
button_div.clicked.connect(set_op_div)
button_eq.clicked.connect(calculate)
button_cls.clicked.connect(clear_screen)

window.show()
app.exec()