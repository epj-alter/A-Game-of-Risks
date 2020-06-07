import csv
import random
from IPython.display import clear_output
from classes.player import Player
from classes.world import World


class Game:
    def __init__(self):
        """
        Initializes the Game object
        """
        # variables
        self.world = World()
        self.n_players = 0
        self.start_troops = 0
        self.players = []
        self.owned_territories = []

        # debug
        self.set_n_players()
        self.init_players()
        self.init_territory_selection()

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
                complain = "Not a valid number!\n"
                pass

    def init_players(self):
        """
        initializes players and their attributes
        generates player's turn randomly
        """
        complain = ""
        players_turn = random.sample(range(self.n_players), self.n_players)
        players_created = {}
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

    def init_territory_selection(self):
        """
        Initializes territory selection phase
        runs until all of the territories in the game world are selected
        """
        complain = ""
        selected_territories = 0
        while selected_territories < len(self.world.territories):
            for i, player in enumerate(self.players):
                selected_territory = None
                while True:
                    clear_output()
                    try:
                        self.world.show_territories()
                        selected_territory = ' '.join([x.capitalize() for x in input(
                            f"{complain}{player.color} player's Turn\nType in the name of one of the territories above, choose wisely!:\n").split()])
                        # updates territory owner
                        # updates player's owned territories and troops
                        if next(x["Owner"] for x in self.world.territories if x["Name"] == selected_territory) == None:
                            self.world.update_territory_data(
                                selected_territory, player.color)
                            self.players[i].add_territory(selected_territory)
                            break
                        else:
                            complain = "Territory has an owner already!\n"
                    except:
                        complain = "Not a valid territory!\n"
                        pass
                selected_territories += 1
