#simple banking system program

def show(balance):
        print(f"\nCurrent Balance: ${balance:.2f}")

def deposit():
    
    amount = float(input("Enter amount to deposit: $"))
    if amount <= 0:
        print("Deposit amount must be positive.")
        return 0

    return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))

    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return 0

    if amount > balance:
        print("Insufficient balance.")
        return 0

    return amount

def main():
    
    balance = 0

    while True:
        print("\n===== Banking System =====")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show(balance)

        elif choice == "2":
            balance += deposit()

        elif choice == "3":
            balance -= withdraw(balance)

        elif choice == "4":
            print("Thank you for using the banking system!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__=='__main__':
    main()