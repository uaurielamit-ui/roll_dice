import backend
import storage
def main():
    end = False
    while not end:
        client_choice = input("""
        ================================
                    ROLL DICE
        ================================

    1. Start New Game
    2. View Game History
    3. View Statistics
    4. Exit

    Choose an option: """) 
        if client_choice == "4":
            end = True
        elif client_choice == "1":
            #backend.start_game()
            game = backend.start_game()
            print_win = game["winner"]
            print (f"the winner is: {print_win}")
            games = storage.load_game_history()
            games.append(game)
            storage.dump_game_history(games)






main()