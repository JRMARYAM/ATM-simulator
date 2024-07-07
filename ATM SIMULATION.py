class ATMMachine:
    def __init__(self, initial_balance=0, pin="5656"):
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

        '''
        1. defining attributes and initialized by default balance and default pin
        2. User is given with the menu to choose the operation to be performed. This includes checking balance, 
        depositing money, changing pin, withdrawl of cash, viewing transaction history and termination of program.
        3. functions of each attributes are declared and defined and main function defined by their respective 
        operations to be performed.
        4. After declaring function main funtion gets called. 
        By using this system user can have track of their accounts.
    
        '''


# function to check balance

    def check_balance(self):
        return self.balance


# function to deposit amount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited successfully. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."


# function to change pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            if len(new_pin) == 4 and new_pin.isdigit():
                 self.pin = new_pin
                 return "PIN changed successfully."
            else:
                 return "New PIN must be a 4-digit number."

        else:
            return  "Old PIN is incorrect."


# function to withdraw amount
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"${amount} withdrawn successfully. New balance: ${self.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."
# function to check transaction history

    def get_transaction_history(self):
        if self.transaction_history:
            return "\n".join(self.transaction_history)
        else:
            return "No transactions yet."
# Main function


def main():
    atm = ATMMachine(10000)  # Initialize ATM with $10000 balance
    while True:
        print("\nATM Machine Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Change Pin")
        print("4. Withdraw Money")
        print("5. View Transaction History")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Your current balance is: ${atm.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == '3':
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            print(atm.change_pin(old_pin, new_pin))
        elif choice == '4':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == '5':
            print("Transaction History:")
            print(atm.get_transaction_history())
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# End of the program


if __name__ == "__main__":
    main()
