import csv
import pandas


class World:
    # debug
    pandas.set_option('display.width', 2000)

    def __init__(self):
        """
        Initializes Game world's data
        """
        # variables
        self.player_colors = list(csv.reader(open("data/colors.csv", "r")))[0]
        self.territories = []
        self.import_territory_data()

    def process_territory_data(self, row: dict) -> list:
        """
        Performs the right data conversions that the game uses
        """
        conversions = {
            "borders": lambda x: x.split("-"),
            "troops": lambda x: 0 if x is None else int(x)
        }

        new_row = {}
        for column, value in row.items():
            if column in conversions:
                new_row[column.capitalize()] = conversions[column](value)
            else:
                new_row[column.capitalize()] = value

        return new_row

    def import_territory_data(self) -> list:
        """
        Reads the data and stores it in a list with raw data values
        Processes and returns the data using a helper function
        """
        reader = csv.DictReader(open("data/territories.csv", "r"))
        self.territories = [self.process_territory_data(x)
                            for x in [k for i, k in enumerate(reader)]]

    def show_territories(self):
        """
        Prints all the territories and its attributes
        """
        # note: create an image with the available territories is for reference.
        print(pandas.DataFrame(self.territories))

    def update_territory_data(self, territory_name: str, new_onwer: str, n_troops=1):
        """
        Updates the territory owner and troops accordingly to the values passed in
        """
        # refactor
        self.territories[[i for i, x in enumerate(self.territories) if x["Name"] == territory_name][0]].update(
            {"Owner": new_onwer, "Troops": n_troops})
