from PySide6.QtWidgets import QApplication, QWidget, QSpinBox, QPushButton, QLabel

app = QApplication()
window = QWidget()
window.setGeometry(100, 100, 400, 250)
window.setStyleSheet('font-size:16px')

input_box = QSpinBox( window)
input_box.setGeometry(100, 30, 200, 40)
input_box.setRange(0, 1000)


result_label = QLabel('Result will appear here', window)
result_label.setGeometry(100, 80, 300, 40)
result_label.setStyleSheet('font-size:16px')

def check_prime():
    num = input_box.value() 
    is_prime = True
    
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
                
    if is_prime:
        result_label.setText(f"{num} is a prime number!")
       
    else:
        result_label.setText(f"{num} is not a prime number.")
       

input_box.valueChanged.connect(check_prime)

window.show()
app.exec()


# הסבר על אלגוריתם בדיקת מספר ראשוני:
    # מספר ראשוני הוא מספר טבעי שגדול מ-1 ומתחלק ללא שארית רק ב-1 ובעצמו.
    # 
    # 1. קודם כל נבדוק אם המספר קטן או שווה ל-1. אם כן, הוא לא ראשוני.
    # 2. .אם הוא גדול מ-1, ננסה לחלק אותו בכל המספרים השלמים החל מ-2 ועד למספר עצמו 
    # 3. ברגע שמצאנו לפחות מספר אחד שהמספר שלנו מתחלק בו ללא שארית 
    #    נדע שהוא לא ראשוני ונעצור את הלולאה.
    # 4. אם סיימנו את הלולאה ולא מצאנו שום מחלק, המספר הוא ראשוני.