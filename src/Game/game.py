import random


def coin_game(account_value: float) -> list:
    amount_wagered = 0.0
    option_selected_by_player = 0
    while True:
        try:
            amount_wagered = float(input("Enter the amount you wish to bet: "))
            if amount_wagered > 0 and amount_wagered <= account_value:
                break
            else:
                print(
                    "\nThe value to be entered must only be a positive numeric value",
                    end="\n\n",
                )
        except ValueError as error:
            print(f"\nAn error has occurred: {error}")
            print("The value entered is not a numeric value")
            print(
                "The value to be entered must only be a positive numeric value",
                end="\n\n",
            )
    while True:
        try:
            options = [1, 2]
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
    coin_result = random.randint(1, 2)
    result = "v" if (coin_result == option_selected_by_player) else "d"
    if result == "v":
        account_value += amount_wagered
        print("The player won")
    else:
        account_value -= amount_wagered
        print("The player lost")
    return [account_value, result]


def slot_game(account_value: float) -> list:
    amount_wagered = 0.0
    while True:
        try:
            amount_wagered = float(input("Enter the amount you wish to bet: "))
            if amount_wagered > 0 and amount_wagered <= account_value:
                break
            else:
                print(
                    "\nThe value to be entered must only be a positive numeric value",
                    end="\n\n",
                )
        except ValueError as error:
            print(f"\nAn error has occurred: {error}")
            print("The value entered is not a numeric value")
            print(
                "The value to be entered must only be a positive numeric value",
                end="\n\n",
            )
    while True:
        try:
            options = [1, 2, 3]
            print("You must enter three different values")
            print("The values ​​must be between 1 and 3", end="\n\n")
            first_value = int(input("Enter the first value here: "))
            second_value = int(input("Enter the second value here: "))
            third_value = int(input("Enter the third value here: "))
            if (
                first_value in options
                and second_value in options
                and third_value in options
            ):
                break
            else:
                print("\nYou must enter only the values ​​from the menu", end="\n\n")
        except ValueError as error:
            print("\nError: The entered value is not a valid option.")
            print(f"An error has occurred: {error}")
            print("You must enter only the values ​​from the menu", end="\n\n")
    random_number = random.randint(1, 3)
    equal_value = 0
    equal_value = equal_value + 1 if (random_number == first_value) else equal_value
    equal_value = equal_value + 1 if (random_number == second_value) else equal_value
    equal_value = equal_value + 1 if (random_number == third_value) else equal_value
    if equal_value == 3:
        result = "v"
        account_value += amount_wagered * 4
        print("The player won")
    elif equal_value == 2:
        result = "v"
        account_value += amount_wagered * 2
        print("The player won")
    elif equal_value == 1:
        result = "v"
        print("The player tied with the casino")
        print(
            "It will be considered a victory for the player, but he will not gain any monetary value",
            end="\n\n",
        )
    else:
        account_value -= amount_wagered
        result = "v"
        print("The player lost")
    return [account_value, result]


def blue_jack(account_value: float) -> list:
    amount_wagered = 0.0
    while True:
        try:
            amount_wagered = float(input("Enter the amount you wish to bet: "))
            if amount_wagered > 0 and amount_wagered <= account_value:
                break
            else:
                print(
                    "\nThe value to be entered must only be a positive numeric value",
                    end="\n\n",
                )
        except ValueError as error:
            print(f"\nAn error has occurred: {error}")
            print("The value entered is not a numeric value")
            print(
                "The value to be entered must only be a positive numeric value",
                end="\n\n",
            )
    first_value_player = random.randint(2, 12)
    second_value_player = random.randint(2, 12)
    first_value_casino = random.randint(2, 12)
    second_value_casino = random.randint(2, 12)
    print(
        f"The cards for the player are: {first_value_player}, {second_value_player}, Sum: {first_value_player + second_value_player}",
        end="\n\n",
    )
    print(f"The first card for the casino is: {first_value_casino}", end="\n\n")
    while True:
        try:
            options = [1, 2]
            print("Select one of the following options", end="\n\n")
            print("1. Play directly")
            print("2. Get another card for the player")
            option_selected_by_player = int(input("Enter the option here: "))
            if option_selected_by_player in options:
                break
            else:
                print("\nYou must enter only the values ​​from the menu", end="\n\n")
        except ValueError as error:
            print("\nError: The entered value is not a valid option.")
            print(f"An error has occurred: {error}")
            print("You must enter only the values ​​from the menu", end="\n\n")
    third_value_player = (
        0 if (option_selected_by_player == "1") else random.randint(2, 12)
    )
    sum_player = first_value_player + second_value_player + third_value_player
    sum_casino = first_value_casino + second_value_casino
    print(f"Player: {sum_player}, Casino: {sum_casino}")
    if sum_casino > 21:
        result = "v"
        account_value += amount_wagered * 1.75
        print("The player won")
    elif sum_casino < 21 and sum_player > 21:
        result = "d"
        account_value += amount_wagered * -1
        print("The player lost")
    elif sum_casino < sum_player:
        result = "v"
        account_value += amount_wagered * 1.50
        print("The player won")
    elif sum_casino == sum_player:
        result = "v"
        print("The player tied with the casino")
        print(
            "It will be considered a victory for the player, but he will not gain any monetary value",
            end="\n\n",
        )
    else:
        result = "d"
        account_value -= amount_wagered
        print("The player lost")
    return [account_value, result]
