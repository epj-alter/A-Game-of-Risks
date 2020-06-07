class Player:
    """
    Handles player creation
    """

    def __init__(self, color, n_troops):
        """
        Creates a new Player
        """
        # variables
        self.color = color
        self.troops = n_troops
        self.territories = []

    def add_troops(self, n_troops: int):
        """
        Adds the specified number of troops to the player
        """
        self.troops += n_troops

    def remove_troops(self, n_troops: int):
        """
        Removes the specified number of troops from the player
        """
        self.troops -= n_troops
        if self.troops < 0:
            self.troops = 0

    def add_territory(self, territory_name: str, n_troops=1):
        """
        Adds a territory to the player
        if n_troops is not identified then 1 is the default value
        """

        self.territories.append({"Name": territory_name, "Troops": n_troops})

    def remove_territory(self, territory_name: str):
        """
        Removes the specified territory from the player
        """
        self.territories = [
            territory for territory in self.territories if territory["Name"] != territory_name]
