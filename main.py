from src.Menu.menu import (
    welcome_menu,
    deposit_amout,
    game_menu,
    exit_game_menu,
    show_statistics,
)
from src.Game.game import coin_game, slot_game, blue_jack


def main():
    welcome_menu()
    account_value = deposit_amout()
    print("------------------------------------------" * 4, end="\n\n")
    exit_game = False
    win_counter = 0
    loss_counter = 0
    game_counter = 0
    while True:
        selected_game = game_menu()
        print("------------------------------------------" * 4, end="\n\n")
        match selected_game:
            case 1:
                result = coin_game(account_value)
            case 2:
                result = slot_game(account_value)
            case 3:
                result = blue_jack(account_value)
        account_value = result[0]
        win_counter = win_counter + 1 if result[1] == "v" else win_counter
        loss_counter = loss_counter if result[1] == "v" else loss_counter + 1
        game_counter += 1
        print("------------------------------------------" * 4, end="\n\n")
        exit_game = exit_game_menu(account_value)
        print("------------------------------------------" * 4, end="\n\n")
        show_statistics(win_counter, loss_counter, game_counter, account_value)
        if exit_game:
            break


if __name__ == "__main__":
    main()
