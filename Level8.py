from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from Level8bank_account import BankAccount


def get_money_amount(prompt):
    """Ask for a positive amount of money and return it as a Decimal."""
    while True:
        user_input = input(prompt)

        try:
            amount = Decimal(user_input).quantize(
                Decimal("0.01"),rounding=ROUND_HALF_UP,)
        
        except InvalidOperation:
            print("Please enter a valid number.")
            continue

        if not amount.is_finite():
            print("Please enter a valid number.")
            continue

        if amount <= 0:
            print("The amount must be greater than zero.")
            continue

        return amount


def make_deposit(account):
    amount = get_money_amount("How much would you like to deposit? $")
    account.deposit(amount)
    print(f"${amount:.2f} was deposited.")


def make_withdrawal(account):
    amount = get_money_amount("How much would you like to withdraw? $")

    if account.withdraw(amount):
        print(f"${amount:.2f} was withdrawn.")
    else:
        print("You cannot withdraw more money than your current balance.")


def view_account_information(account):
    account.display_information()


def display_menu():
    print("\nPlease choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")


def main():
    print("Welcome to the Bank!")

    customer_name = input("Please enter your name: ").strip()
    while not customer_name:
        print("Name cannot be blank.")
        customer_name = input("Please enter your name: ").strip()

    account = BankAccount(customer_name)

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            make_deposit(account)
        elif choice == "2":
            make_withdrawal(account)
        elif choice == "3":
            view_account_information(account)
        elif choice == "4":
            print("Thank you for your business!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()