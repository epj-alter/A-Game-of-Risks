from IPython.display import clear_output
from core.player import Player
from core.data import player_colors
import random


class Game:

    # Variables
    n_players = 0
    start_troops = 0
    players = []

    def __init__(self):
        """
        Creates a new Game
        """
        # debug
        self.set_n_players()
        self.init_players()
        print([x.color for x in self.players])

    def set_n_players(self):
        """
        Sets the number of players in the Game
        """
        while True:
            clear_output()
            try:
                self.n_players = int(
                    input("Please insert the number of players (between 2 to 6): \n"))
                if self.n_players >= 2 and self.n_players < 7:
                    self.start_troops = 120 / self.n_players
                    break
                elif self.n_players < 2:
                    self.n_players = print("Not enough players!")
                elif self.n_players >= 7:
                    self.n_players = print("Too many players!")
            except:
                pass

        print(f"The number of players is {self.n_players}")
        print(f"The number of troops is {self.start_troops}")

    def init_players(self):
        """
        initializes players and their attributes
        generates player's turn randomly
        """
        players_turn = random.sample(range(self.n_players), self.n_players)
        players_created = {}
        # debug
        print(players_turn)
        picked_colors = []
        for x in range(self.n_players):
            while True:
                try:
                    color = input(
                        f"Player {x+1}, please type in one of the following colors: ({', '.join([x for x in player_colors if x not in picked_colors])}):\n").capitalize()
                    if color in player_colors and color not in picked_colors:
                        picked_colors.append(color)
                        players_created[players_turn[x]] = Player(
                            color, self.start_troops)
                        break
                    else:
                        print("Color is currently not available :(")
                except:
                    pass

        self.players = [players_created[y] for x in range(
            self.n_players) for y in players_created.keys() if int(y) == x]
