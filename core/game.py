from IPython.display import clear_output


class Game:

    n_players = 0

    def set_n_players(self):
        while True:
            clear_output()
            try:
                self.n_players = int(
                    input("Please insert the number of players (between 2 to 5): "))
                if self.n_players >= 2 and self.n_players < 6:
                    break
                elif self.n_players < 2:
                    self.n_players = print("Not enough players!")
                elif self.n_players >= 6:
                    self.n_players = print("Too many players!")
            except:
                pass

        print(f"The number of players is {self.n_players}")
