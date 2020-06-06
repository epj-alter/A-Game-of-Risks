import csv
import random
from IPython.display import clear_output
from classes.player import Player
from classes.world import World


class Game:

    # Variables
    world = World()
    n_players = 0
    start_troops = 0
    players = []
    owned_territories = []

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
        complain = ""
        while True:
            clear_output()
            try:
                self.n_players = int(
                    input(f"{complain}Please insert the number of players (between 2 to 6): \n"))
                if self.n_players >= 2 and self.n_players < 7:
                    self.start_troops = 120 / self.n_players
                    break
                elif self.n_players < 2:
                    complain = "Not enough players!\n"
                elif self.n_players >= 7:
                    complain = "Too many players!\n"
            except:
                pass

    def init_players(self):
        """
        initializes players and their attributes
        generates player's turn randomly
        """
        complain = ""
        players_turn = random.sample(range(self.n_players), self.n_players)
        players_created = {}
        # debug
        print(players_turn)
        picked_colors = []
        for x in range(self.n_players):
            while True:
                clear_output()
                try:
                    color = input(
                        f"{complain}Player {x+1}, please type in one of the following colors: ({', '.join([x.capitalize() for x in self.world.player_colors if x not in picked_colors])}):\n").lower()
                    if color in self.world.player_colors and color not in picked_colors:
                        picked_colors.append(color)
                        players_created[players_turn[x]] = Player(
                            color.capitalize(), self.start_troops)
                        break
                    else:
                        complain = "Please enter a valid color\n"
                except:
                    pass

        self.players = [players_created[y] for x in range(
            self.n_players) for y in players_created.keys() if int(y) == x]
