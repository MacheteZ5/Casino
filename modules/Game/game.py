import random

def coin_game(account_value : float) -> list:
    amount_wagered = 0.0
    option_selected_by_player = 0
    while True:
        try:
            amount_wagered = float(input("Enter the amount you wish to bet: "))
            if(amount_wagered > 0 and amount_wagered <= account_value):
                break
            else:
                print("\nThe value to be entered must only be a positive numeric value",  end="\n\n")
        except ValueError as error:
            print(f"\nAn error has occurred: {error}")
            print("The value entered is not a numeric value")
            print("The value to be entered must only be a positive numeric value", end="\n\n")
    while True:
        try:
            options = [1,2]
            print("Select heads or tails", end="\n\n")
            print("1. Heads")
            print("2. Tails")
            option_selected_by_player = int(input("Enter the option here: "))
            if option_selected_by_player in options:
                break
            else:
                print("\nYou must enter only the values ​​from the menu", end="\n\n")
        except ValueError as error:
            print("\nError: The entered value is not a valid option.")
            print(f"An error has occurred: {error}")
            print("You must enter only the values ​​from the menu", end="\n\n")
    coin_result = random.randint(1,2)
    result = "v" if (coin_result == option_selected_by_player) else "d"
    if (result == "v"):
        account_value += amount_wagered
        print("The player won")
    else:
        account_value -= amount_wagered
        print("The player lost")
    return [account_value, result]

def slot_game(account_value: float) -> list:
    pass

def blue_jack(account_value: float) -> list:
    pass
