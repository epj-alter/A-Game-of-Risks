from game import core
from game.player import Player

player1 = Player("blue", 20)

print(player1.color)
print(core.simulate_battle())
