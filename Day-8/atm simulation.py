# ATM Simulation
# Create a simple ATM program with:
# - Check balance
# - Deposit money
# - Withdraw money
# - Exit
# Keep the menu running until the user chooses Exit.

print("Welcome user! How can I help you today? ")
print("1. Check balance")
print("2. Deposit money")
print("3. Withdraw money")
print("4. Exit")
current_balance=1200000.00

while True:

    user_input=(int(input("Please choose your option: ")))

    if user_input==1:

        print("You current balance is: ",current_balance)

    elif user_input==2:

        amount=(int(input("Enter your amount: ")))
        current_balance=current_balance+amount
        print("Money deposited !")
        print("Your balance is: ",current_balance)

    elif user_input==3:

        withdrawl_amount=(int(input("Enter your amount: ")))

        if current_balance>withdrawl_amount:

            print("claim your cash!")
            remaining_balance=current_balance-withdrawl_amount
            print("You remaining balance: ",remaining_balance)
            
        else:

            print("Insufficient balance!")
            print("Your balance is: ",current_balance)
            
    elif user_input==4:

        print("Thank you for using! See you soon...")
        break

    else:

        print("Invalid option! Please choose the correct option.")