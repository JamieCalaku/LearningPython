# Exercise 1 from lesson 42
# Simple Banking program

def show_balance(balance):
    print("**********************")
    print(f"Your current balance is: ${balance:.2f}")
    print("**********************")

def deposit():
    print("**********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("**********************")

    if amount <= 0:
        print("**********************")
        print("That's not a valid amount")
        print("**********************")

        return 0
    else:
        return amount

def withdraw(balance):
    print("**********************")
    amount = float(input("Enter an amount to be withdrawn: "))
    print("**********************")

    if amount > balance:
        print("**********************")
        print("Insufficient funds")
        print("**********************")

        return 0
    elif amount <= 0:
        print("**********************")
        print("That's not a valid amount")
        print("**********************")

        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True

    while is_running:
        print("**********************")
        print("    Banking Program   ")
        print("**********************")

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("**********************")

        choice = input("Enter your choice: ")
        print()

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print("**********************")
                print("That is not a valid choice")
                print("**********************")
    print("**********************")
    print("Thank you! Have a nice day!")
    print("**********************")


if __name__ == "__main__":
    main()