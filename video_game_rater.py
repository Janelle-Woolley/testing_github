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
    for game, rating in dictionary.items():
        print("Game: {}\tRating: {}".format(game, rating))

if __name__ == "__main__":
    video_games = {"Minecraft":5, "Call of Duty":1, "Angry Birds":4,
                   "Splatoon 2":5, "Animal Crossing":4}

    print_dictionary(video_games)
