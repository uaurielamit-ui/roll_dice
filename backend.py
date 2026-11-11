from random import randint
import val

def player_name():
    legal_choice= False
    while not legal_choice:
        name = input("enter your name: ").strip()
        if name != "":
            legal_choice = True
    return name

def how_m_rounds():
    legal_choice = False
    while not legal_choice:
        client_choice = val.int_val("chouse how many round you wont btween 1-10: ")
        if client_choice <=10 and client_choice >=1:
            legal_choice = True
    return client_choice


def roll_dice():
    resolt = randint(1,6)
    return resolt


def calculate_winner(player_score, computer_score):
    winner = ""
    if player_score > computer_score:
        winner ="you wonn"
    elif computer_score > player_score:
        winner = "computer wonn"
    else:
        winner = "no winner this time"
    return winner
    
    


def play_round():
    # staet = input("press enter to roll the dise: ")
    player = roll_dice()
    comp = roll_dice()
    return player, comp


def start_game(): 
    data = {"player":0, "computer":0}
    up_data = {}
    game_num = 0
    name = player_name()
    rounds = how_m_rounds()
    up_data ["player_name"]= name
    up_data["rounds"]= rounds
    up_data["results"]=[]
    while rounds != 0:
        winn_raund = None    #מה זה  
        game_num += 1
        player, computer = play_round()
        if player > computer:
            data["player"]+=1
            winn_raund = name
        if computer > player:
            data["computer"]+=1
            winn_raund = "computer"
        print(f"round number {game_num}")
        print(f"you have  {player} , the computer have {computer} the winner is {winn_raund}")

        up_data["results"].append({
            "round": game_num,
            "player_dice": player,
            "computer_dice": computer,
            "winner": winn_raund})
        rounds -=1
    winner = calculate_winner(data["player"], data["computer"])
    up_data["player_score"]= player
    up_data["computer_score"]= computer
    up_data["winner"]= winner
    return up_data


