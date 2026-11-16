class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0
        self.history = [0]
    
    def deposit(self, amount):
        self.balance += amount
        self.history.append(self.balance)
        
    def withdraw(self, amount):
        if amount > self.balance:
            return 0
        else:
            self.balance -= amount
            self.history.append(self.balance)
            return amount

if __name__ == "__main__":
    my_account = Account("1234")
    print(my_account.balance)
    
    my_account.deposit(5234)
    print(my_account.balance)
    
    my_account.deposit(500)
    print(my_account.balance)
    
    my_account.withdraw(2000)
    print(my_account.balance)
    
    my_account.withdraw(2000)
    print(my_account.balance)