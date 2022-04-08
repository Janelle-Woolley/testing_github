##
# video_game_rater.py
# rates video games
#
# Author: Janelle Woolley
# 08/04/22 Version_1

def print_dictionary(dictionary):
    """
    Accepts a dictionary, loops through it and prints
    out game and it's rating
    """
    # outer dictionary
    for id, game in dictionary.items():
        print("Id: {} Game: {}\tRating: {}".format(id,
                                                    game["name"],
                                                    game["rating"]))

if __name__ == "__main__":
    video_games = {1:{"name":"Minecraft", "rating":5},
                   2:{"name":"Call of Duty", "rating":1},
                   3:{"name":"Angry Birds", "rating":4},
                   4:{"name":"Splatoon 2", "rating":5},
                   5:{"name":"Animal Crossing", "rating":4}}

    print_dictionary(video_games)
