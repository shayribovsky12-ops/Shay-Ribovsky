from PySide6.QtWidgets import QApplication, QWidget, QDoubleSpinBox ,QPushButton, QLabel


app= QApplication() 
window= QWidget()
window.setGeometry(50, 50, 600, 300)
window.setStyleSheet('font-size:16px')

button_ten = QPushButton('10%', window)
button_ten.setGeometry(380, 20, 80, 30)
button_ten.setStyleSheet('font-size: 20px')

button_twenty = QPushButton('20%', window)
button_twenty.setGeometry(380, 50, 80, 30)
button_twenty.setStyleSheet('font-size: 20px')

price = QDoubleSpinBox( window)
price.setGeometry(150, 30, 200, 30)
price.setRange(0, 100000)

text_the_price_is = QLabel("the price is:", window)
text_the_price_is.setGeometry(30, 30, 110, 30)

text_the_tip_is = QLabel("the tip is:", window)
text_the_tip_is.setGeometry(30, 90, 110, 30)

text_the_pricetip_is = QLabel("the price + tip:", window)
text_the_pricetip_is.setGeometry(30, 120, 110, 30)

price_tip = QLabel(window)
price_tip.setGeometry(180,120, 150, 30)
price_tip.setStyleSheet('background-color: lightgray')
price_tip.setText("the price + tip:")

tip = QLabel(window)
tip.setGeometry(180,90, 150, 30)
tip.setStyleSheet('background-color: lightgray')
tip.setText("the tip amount:")

def ten_percent():
    value1 = price.value()
    result = value1 * 1.1
    price_tip.setText(str(result))
    tip.setText(str(value1 * 0.1))

def twenty_percent():
    value1 = price.value()
    result = value1 * 1.2
    price_tip.setText(str(result))
    tip.setText(str(value1 * 0.2))

       
button_ten.clicked.connect(ten_percent)
button_twenty.clicked.connect(twenty_percent)

window.show()
app.exec()