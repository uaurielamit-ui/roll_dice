import json


def load_game_history():
    with open ("game_history.json", "r") as file:
        games = json.load(file)
    return games


def dump_game_history(data):
    with open ("game_history.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


# def save_game_history(data):
#     games = load_game_history()
#     games.append(data)
#     print(games)
#     dump_game_history(games)










#     # with open ("game_history.json", "w", encoding="utf8") as add:


# #     # Get (read) Content from Json file
# #     with open("game_history.json","r",encoding="utf8") as f:
# #         results = json.loads(f.read())
# #         results.append("fdsfsdf")
# #         print(results)



# #     # reWrite content in json file
# #     pass

# load_game_history()