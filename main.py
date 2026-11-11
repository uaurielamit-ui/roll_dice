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
            print (f"the winner is: {print_win} you have: {game["player_score"]}points,  the computer have: {game["computer_score"]} points")
            games = storage.load_game_history()
            games.append(game)
            storage.dump_game_history(games)
        if client_choice == "2":
            game_history = storage.load_game_history()
            backend.display_game_history(game_history)
        if client_choice == "3":
            game_history = storage.load_game_history()
            backend.display_statistics(game_history)






main()