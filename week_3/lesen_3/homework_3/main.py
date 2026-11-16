from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox
from About import AboutWindow
from Account import Account

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.accounts = {}
        self.about_window = AboutWindow()
        self.Bank_Manager()

    def Bank_Manager(self):
        self.setWindowTitle("Bank Accounts Manager")
        self.setGeometry(100, 100, 450, 350)
        self.setStyleSheet("background-color: lightgrey;")

        self.id_label = QLabel("ID:", self)
        self.id_label.setGeometry(20, 20, 50, 30)

        self.id_input = QLineEdit(self)
        self.id_input.setGeometry(60, 20, 120, 30)

        self.open_btn = QPushButton("open Accounts", self)
        self.open_btn.setGeometry(190, 20, 100, 30)
        self.open_btn.clicked.connect(self.open_account_clicked)

        self.combo_label = QLabel("Select Account:", self)
        self.combo_label.setGeometry(20, 70, 100, 30)

        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(120, 70, 120, 30)
        self.combo_box.currentTextChanged.connect(self.account_selected)

        self.balance_title = QLabel("Balance:", self)
        self.balance_title.setGeometry(20, 120, 60, 30)

        self.balance_label = QLabel("0", self)
        self.balance_label.setGeometry(80, 120, 100, 30)

        self.amount_label = QLabel("Amount:", self)
        self.amount_label.setGeometry(20, 170, 60, 30)

        self.amount_input = QLineEdit(self)
        self.amount_input.setGeometry(80, 170, 100, 30)

        self.deposit_btn = QPushButton("Deposit", self)
        self.deposit_btn.setGeometry(190, 170, 80, 30)
        self.deposit_btn.clicked.connect(self.deposit_clicked)

        self.withdraw_btn = QPushButton("Withdraw", self)
        self.withdraw_btn.setGeometry(280, 170, 80, 30)
        self.withdraw_btn.clicked.connect(self.withdraw_clicked)

        self.msg_label = QLabel("", self)
        self.msg_label.setGeometry(20, 220, 350, 30)

        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(20, 270, 100, 40)
        self.about_button.clicked.connect(self.about_clicked)

    def open_account_clicked(self):
        account_id = self.id_input.text()
        
        if account_id in self.accounts:
            self.msg_label.setText("Account already exists!")
        elif account_id != "":
            new_account = Account(account_id)
            self.accounts[account_id] = new_account
            self.combo_box.addItem(account_id)
            self.msg_label.setText("Account opened successfully!")
            self.id_input.clear()
            self.amount_input.clear()
            self.combo_box.setCurrentText(account_id)

    def account_selected(self, account_id):
        if account_id in self.accounts:
            acc = self.accounts[account_id]
            self.balance_label.setText(str(acc.balance))
            self.msg_label.setText("")

    def deposit_clicked(self):
        account_id = self.combo_box.currentText()
        if account_id in self.accounts:
            amount = int(self.amount_input.text())
            self.accounts[account_id].deposit(amount)
            self.balance_label.setText(str(self.accounts[account_id].balance))
            self.amount_input.clear()
    def withdraw_clicked(self):
        account_id = self.combo_box.currentText()
        if account_id in self.accounts:
            amount = int(self.amount_input.text())
            withdrawn = self.accounts[account_id].withdraw(amount)

            if withdrawn == 0:
                self.msg_label.setText("the operation failed!")
            else:
                self.balance_label.setText(str(self.accounts[account_id].balance))
                self.amount_input.clear()
                self.msg_label.setText("")
    def about_clicked(self):
        self.about_window.show()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()