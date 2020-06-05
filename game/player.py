class Player:
    """
    Handles player creation
    """

    def __init__(self, color: str, n_troops: int):
        self.color = color
        self.troops = n_troops
        self.territories = {}

    def add_troops(self, n_troops: int):
        self.troops += n_troops

    def remove_troops(self, n_troops: int):
        self.troops -= n_troops
        if self.troops < 0:
            self.troops = 0

    def add_territory(self, territory: tuple):
        self.territories[territory[0]] = territory[1]

    def remove_territory(self, territory_name: str):
        self.territories.pop(territory_name)
