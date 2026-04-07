def welcome_menu() -> None:
    print("Welcome to Silver and Gold Casino")
    print("Have fun in the three different games offered by our Casino")
    print(
        "First of all, you must deposit an amount into your account in order to play",
        end="\n\n",
    )


def deposit_amout() -> float:
    account_value = 0.0
    while True:
        try:
            account_value = float(
                input("Enter the amount you wish to add to your account: ").strip()
            )
            if account_value > 0:
                break
            else:
                print(
                    "\n\n The value to be entered must only be a positive numeric value",
                    end="\n\n",
                )
        except ValueError as error:
            print(f"\n\nAn error has occurred: {error}")
            print("The value entered is not a numeric value")
            print(
                "The value to be entered must only be a positive numeric value",
                end="\n\n",
            )
    return account_value


def game_menu() -> int:
    while True:
        options = ["1", "2", "3"]
        print(
            "Select one of the following games offered by our casino to play",
            end="\n\n",
        )
        print("1. Coin Game (Heads or Tails)")
        print("2. Slot Game")
        print("3. 21 Blue Jack")
        option = input("Enter the option here: ").strip()
        if option in options:
            break
        else:
            print("\n\nYou must enter only the values ​​from the menu", end="\n\n")
    return int(option)


def show_statistics(
    win_counter: int, loss_counter: int, game_counter: int, account_value: int
):
    print(f"Number of games played: {game_counter}")
    print(f"Number of games won: {win_counter}")
    print(f"Number of games lost: {loss_counter}")
    print(
        f"Final amount in account: {0 if account_value < 0 else account_value}",
        end="\n\n",
    )


def exit_game_menu(account_value: float) -> bool:
    exit_game = True if (account_value <= 0) else False
    if not exit_game:
        exit_game = exit_game_menu_by_player()
    return exit_game


def exit_game_menu_by_player() -> bool:
    while True:
        options = ["1", "2"]
        print("Do you want to exit the game?", end="\n\n")
        print(" 1. Yes\n 2. No", end="\n\n")
        option = input("Enter the option here: ").strip()
        if option in options:
            break
        else:
            print("\n\nYou must enter only the values ​​from the menu", end="\n\n")
    return True if (option == "1") else False
