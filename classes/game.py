import pandas
import csv
import random
from IPython.display import clear_output
from classes.player import Player
from classes.world import World


class Game:
    def __init__(self):
        """
        Resets the Game
        """
        # variables
        self.world = World()
        self.n_players = 0
        self.start_troops = 0
        self.players = []
        self.owned_territories = []

    def start(self):
        """
        Starts the game loop
        """
        self.__init__()
        self.set_n_players()
        self.init_players()
        self.init_territory_selection_phase()
        self.init_troop_deployment_phase()
        # self.game_phase()

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

    def init_territory_selection_phase(self):
        """
        Initializes territory selection phase
        runs until all of the territories in the game world are selected
        """
        phase_name = "Territory Selection Phase!\n\n"
        selected_territories = 0
        while selected_territories < len(self.world.territories):
            for i, player in enumerate(self.players):
                complain = ""
                selected_territory = None
                while True:
                    clear_output()
                    self.world.show_territories()
                    try:
                        selected_territory = ' '.join([x.capitalize() for x in input(
                            f"{phase_name}{complain}{player.color} player's Turn\nType in the name of one of the territories displayed, choose wisely!:\n").split()])
                        # updates territory owner
                        # updates player's owned territories and troops
                        if next(x["Owner"] for x in self.world.territories if x["Name"] == selected_territory) == None:
                            self.world.update_territory_data(
                                selected_territory, player.color)
                            self.players[i].add_territory(selected_territory)
                            self.players[i].remove_troops(1)
                            break
                        else:
                            complain = "Territory has an owner already!\n"
                    except:
                        complain = "Not a valid territory!\n"
                        pass
                selected_territories += 1

    def init_troop_deployment_phase(self):
        phase_name = "Troop Deployment Phase!"
        # while any player has more than 0 troops
        while any(x for x in self.players if x.troops > 0):
            for i, player in enumerate(self.players):
                complain = ""
                troops_to_assign = 3  # shoud be 3
                if player.troops < 3:
                    troops_to_assign = player.troops
                while player.troops > 0:
                    clear_output()
                    self.world.show_territories()
                    try:
                        print(f"{phase_name}\n")
                        print(
                            f"You have {int(player.troops)} Troops left.\n")
                        selected_territory = ' '.join([x.capitalize() for x in input(
                            f"{complain}{player.color} player's Turn\nType in the name of one of your territories:\n").split()])
                        if next(x["Owner"] for x in self.world.territories if x["Name"] == selected_territory) == player.color:
                            self.world.update_territory_data(
                                selected_territory, player.color, troops_to_assign)
                            self.players[i].remove_troops(troops_to_assign)
                            break
                        else:
                            complain = "This territory does not belong to you!\n"
                    except:
                        complain = "Not a valid territory!\n"
                        pass

    def game_phase(self):
        while any(player for player in self.players if len(player.territories) <= len(self.world.territories)):
            # turn start
            for i, player in enumerate(self.players):
                complain = ""
                # adds the turn troops to the player
                troops = 1 + int(len(player.territories) / 3)
                player.add_troops(troops)
                # deploying phase
                while len(player.territories) > 0:
                    try:
                        clear_output()
                        print(
                            f"{'Troop Deployment Phase! Type in Next to skip.'}\n\n")
                        print(f"{complain}\n")
                        self.world.show_territories()
                        # ask the player for a territory, or to skip
                        action = ' '.join([x.capitalize() for x in input(
                            f"{player.color} player's Turn\n You have {player.troops} Troops.\nType in the territory you want to assign troops to:\n").split()])
                        # break if next
                        if action == "Next":
                            break
                        # ask for the number of troops to deploy
                        troops_to_assign = int(
                            input(f"{complain}Please insert the number of Troops you want to assign: \n"))
                        if player.troops < troops_to_assign:
                            complain = "Not enough Troops!\n"
                            break
                        if next(x["Owner"] for x in self.world.territories if x["Name"] == action) == player.color:
                            self.world.update_territory_data(
                                action, player.color, troops_to_assign)
                            self.players[i].remove_troops(troops_to_assign)
                        else:
                            complain = "This territory does not belong to you!\n"
                    except:
                        complain = "Not a valid territory!\n"
                        pass

                complain = ""
                # attacking phase
                while True:
                    clear_output()
                    # set territories to use
                    player_territories = [
                        z for x in player.territories for z in self.world.territories if x in z["Name"]]
                    enemy_territories = [y for x in player_territories for y in self.world.territories if x["Name"]
                                         in y["Borders"] and x["Owner"] not in y["Owner"]]
                    available_territories = {
                        x["Name"]: x["Troops"] for x in player_territories for y in enemy_territories if x["Name"] in y["Borders"]}
                    # select own territory for attack
                    print(
                        f"{'Attacking Phase'}\n\n{complain}{player.color} player's Turn\nType in the name of the territory you want to use! type in 'end' to end your turn:\n")
                    selected_territory = ' '.join([x.capitalize() for x in input(
                        f"{available_territories} troops\n").split()])
                    if selected_territory == "End":
                        break
                    # select enemy territory to attack
                    print(
                        f"{pandas.DataFrame([x for x in enemy_territories if selected_territory in x['Borders']])}")
                    territory_to_attack = ' '.join([x.capitalize() for x in input(
                        f"Type in a territory to attack:\n").split()])
                    # calculate the battle
                    ally = next(
                        x["Troops"] for x in self.world.territories if x["Name"] == selected_territory)
                    enemy = next(
                        x["Troops"] for x in self.world.territories if x["Name"] == territory_to_attack)
                    while True:
                        result = random.choice([0, 1])
                        if result == 0:
                            ally -= 1
                            self.world.update_territory_data(
                                selected_territory, player.color, -1)
                        elif result == 1:
                            enemy -= 1
                        if ally <= 1:
                            self.world.update_territory_data(
                                selected_territory, player.color, -(ally-1))
                            print("Ally Lost!")
                            break
                        elif enemy < 1:
                            self.world.update_territory_data(
                                territory_to_attack, player.color, ally-1)
                            print("Ally Won!")
                            break

        return f"{''.join([player.color for player in self.players if len(player.territories) >= len(self.world.territories)])} won!"
