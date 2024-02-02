class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def login(self, entered_pin):
        if entered_pin == self.pin:
            print("Login successful!")
            return True
        else:
            print("Incorrect PIN. Login failed.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._add_transaction("Deposit", amount)
            print(f"Deposit successful. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self._add_transaction("Withdrawal", amount)
            print(f"Withdrawal successful. Current balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def view_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def _add_transaction(self, transaction_type, amount):
        transaction = f"{transaction_type}: ${amount}"
        self.transaction_history.append(transaction)

# Example usage with menu:
account1 = BankAccount(account_number="123456789", pin="1234")

while True:
    print("\nMenu:")
    print("1. Login")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Check Balance")
    print("5. View Transaction History")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        entered_pin = input("Enter your PIN: ")
        account1.login(entered_pin)
    elif choice == "2":
        amount = float(input("Enter the deposit amount: "))
        account1.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter the withdrawal amount: "))
        account1.withdraw(amount)
    elif choice == "4":
        account1.check_balance()
    elif choice == "5":
        account1.view_transaction_history()
    elif choice == "6":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
