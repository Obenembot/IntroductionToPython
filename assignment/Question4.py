def create_account(account_number: int, account_type: str, min_balance: float, current_balance: float):
    print(f"\n$$$$$$$$$$$$$$$$$$$$ Account Number: {account_number} $$$$$$$$$$$$$$$$$$$$")
    if account_type == 's':  # saving account type block
        print(f"Selected Account Type Is 'Savings'")
        if current_balance > min_balance:
            print(f"Current Balance: ${current_balance} Is Greater Than Min Balance: ${min_balance}.")
            print(f"4% Interest Will Be Added To The ${current_balance} Balance")
            # Customer get a 4% increase is the current balance is more than the min balance.
            interest_percent = 4 / 100
            interest = interest_percent * current_balance
            new_current_balance = interest + current_balance
            print(f"Interest Yielded Is : ${interest}")
            print(f"New Current Balance: ${new_current_balance}")
        else:
            # Customer get charge $10.00 incase the min balance is more than the current balance
            saving_account_service_fee: float = 10.00
            print(f"Current Balance: ${current_balance} Is Lesser Than Min Balance: ${min_balance}.")
            print(f"A Service Fee Of ${saving_account_service_fee} Will Be Applied")
            new_current_balance = current_balance - saving_account_service_fee
            print(f"New Current Balance: ${new_current_balance}")
    elif account_type == 'c':  # check account type block
        print(f"Selected Account Type Is 'Check'")
        if min_balance > current_balance:
            # Customer get charge $25.00 incase the min balance is more than the current balance
            saving_account_service_fee: float = 25.00
            print(f"Current Balance: ${current_balance} Is Lesser Than Min Balance: ${min_balance}.")
            print(f"A Service Fee Of ${saving_account_service_fee} Will Be Applied")
            new_current_balance = current_balance - saving_account_service_fee
            print(f"New Current Balance: ${new_current_balance}")
        else:
            if (
                    current_balance - min_balance) <= 5000:  # check is the diff between current balance and min_balance is less or equal to 5000
                interest = (3 / 100) * current_balance
                print(f"3% Interest ${interest} will be applied to current balance ${current_balance}")
            else:
                interest = (5 / 100) * current_balance
                print(f"5% Interest ${interest} will be applied to current balance ${current_balance}")
            new_current_balance = current_balance + interest
            print(f"New Current Balance: ${new_current_balance}")
    else:
        print(f"Invalid account type provided ${account_type}")


# Use while loop to make sure to capture user input
if __name__ == "__main__":
    account_number = input("Enter Account Number: ")
    while account_number == "":
        account_number = input("Enter Account Number: ")

    account_type = input("Enter Account Type (s for savings, c for checking): ")
    while account_type not in ('s', 'c'):
        account_type = input("Enter Account Type (s for savings, c for checking): ")

    min_balance = input("Enter Minimum Balance: ")
    while min_balance == "":
        min_balance = input("Enter Minimum Balance: ")

    current_balance = input("Enter current balance: ")
    while current_balance == "":
        input("Enter current balance: ")

    # invoke the create_account method.
    create_account(int(account_number), account_type, float(min_balance), float(current_balance))
