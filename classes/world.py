import csv


class World:

    # variables
    player_colors = list(csv.reader(open("data/colors.csv", "r")))[0]
    territories = []

    def __init__(self):
        self.import_territory_data()

    def process_territory_data(self, row: dict) -> list:

        # perform the right data conversion for the game to use
        conversions = {
            "borders": lambda x: x.split("-"),
            "troops": lambda x: 0 if x is None else int(x)
        }

        new_row = {}
        for column, value in row.items():
            if column in conversions:
                new_row[column] = conversions[column](value)
            else:
                new_row[column] = value

        return new_row

    def import_territory_data(self) -> list:
        # read the data and store it in a list with raw data
        reader = csv.DictReader(open("data/territories.csv", "r"))
        # process and return the data using our helper function
        self.territories = [self.process_territory_data(x)
                            for x in [k for i, k in enumerate(reader)]]
