import random


def coin_game(account_value: float) -> list:
    amount_wagered = __validate_entrey_amount_bet(account_value)
    option_selected_by_player = __game_options("coin_game")
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
    amount_wagered = __validate_entrey_amount_bet(account_value)
    first_value = random.randint(1, 3)
    second_value = random.randint(1, 3)
    third_value = random.randint(1, 3)
    if first_value == second_value == third_value:
        result = "v"
        account_value += amount_wagered * 4
        print("The player won")
    elif len({first_value, second_value, third_value}) < 3:
        result = "v"
        account_value += amount_wagered * 2
        print("The player won")
    else:
        account_value -= amount_wagered
        result = "v"
        print("The player lost")
    return [account_value, result]


def blue_jack(account_value: float) -> list:
    amount_wagered = __validate_entrey_amount_bet(account_value)
    first_value_player = random.randint(2, 12)
    second_value_player = random.randint(2, 12)
    first_value_casino = random.randint(2, 12)
    second_value_casino = random.randint(2, 12)
    print(
        f"The cards for the player are: {first_value_player}, {second_value_player}, Sum: {first_value_player + second_value_player}",
        end="\n\n",
    )
    print(f"The first card for the casino is: {first_value_casino}", end="\n\n")
    option_selected_by_player = __game_options("blue_jack")
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


def __validate_entrey_amount_bet(account_value: float) -> float:
    while True:
        try:
            amount_wagered = float(input("Enter the amount you wish to bet: "))
            if 0 < amount_wagered <= account_value:
                return amount_wagered
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


def __game_options(game_type) -> int:
    while True:
        try:
            options = [1, 2]
            print("Select one of the following options", end="\n\n")
            print("1. Play directly" if game_type == "blue_jack" else "1. Heads")
            print(
                "2. Get another card for the player"
                if game_type == "blue_jack"
                else "2. Tails"
            )
            option_selected_by_player = int(input("Enter the option here: "))
            if option_selected_by_player in options:
                return option_selected_by_player
            else:
                print("\nYou must enter only the values ​​from the menu", end="\n\n")
        except ValueError as error:
            print("\nError: The entered value is not a valid option.")
            print(f"An error has occurred: {error}")
            print("You must enter only the values ​​from the menu", end="\n\n")
