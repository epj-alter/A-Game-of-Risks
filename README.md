<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Project: A Game of Risks

_[DATA ANALYTICS FULL TIME, Berlin & jun.2020]_

## Content

- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description

This is a basic version of the popular game **Risk**, also themed like **Game of Thrones** because I really like their fantasy world.

I really like the game and the difficulty of emulating it, it is a great challenge for my current python skills.

## Overview

### Game Start

- The game will ask how many players are going to play the game (min 2 max 6)
- The number of starting troops per player is 120 divided by the number of players

  - If 2 are playing, each player counts out 60 troops
  - If 3 are playing, each player counts out 40 Troops.
  - If 4 are playing, each player counts out 30 Troops.
  - If 5 are playing, each player counts out 24 Troops.
  - If 6 are playing, each player counts out 20 Troops.

- Turn order is randomly selected.

- Each player by turn has to select a territory by typing in the territory's name,
  there is also an option to just type in the territory's region and you will be assigned a random territory in that region.

- After all territories are claimed troop deployment round starts, allowing each player by turn to add a bulk of troops to the territory
  of their choice until players run out of troops.

### Gameplay

- The objective of the game is to conquer the world by occupying all territories on the board. You need to eliminate all your opponents.

- On your turn, try to capture territories by defeating your opponents' armies. But be careful: Winning battles will depend on careful planning, quick decisions, and bold moves.
  You will have to place your forces wisely, attack at just the right time and fortify your defenses against all enemies.

- You will get a number of troops at the start of your turn, the number of troops is calculated in the following manner:

  - The number of territories you occupy divided by 3, ignoring any fraction.
  - The value of the region you control. The number of extra armies is different for each region:
    - The North: 4
    - King's Lands: 5
    - The South: 3
    - The Free Cities: 5
    - The Dothraki: 3
    - The Shadow Lands: 4

- After placing your armies at the beginning of your turn, decide if you wish to attack at this time. The object of an attack is to capture a territory,
  by defeating all the opposing armies already on it. The battle is fought by a roll of the dice. Study the map for a moment. Do you want to attack? - You may only attack a territory that's adjacent (touching) to one of your own. - You must always have at least two armies in the territory you're attacking from. - You may continue attacking one territory until you have eliminated all armies on it, or you may shift your attack from one territory to another,
  attacking each as often as you want and attacking as many territories as you like during one turn.

- No matter what you have done on your turn, you may end your turn by fortifying your position.
  - You are not required to win a battle or even to try an attack to do so.
  - To fortify your position, move as many armies as you would like from one (and only one) of your territories
    into one (and only one) of your adjacent territories.
  - Remember to move troops towards borders where they can help in an attack and leave at least one army behind.

## Workflow

- Create the data containing the regions and each of their attributes
  - Regions
  - Territories
- Create the Player class
- Create the Game Class
  - Add a function to set the number of players
  - Add a function to set the attributes of players (player color and the number of starting troops)
  - Add a function to random player's turn order

## Organization

- Used trello so I could organize and focus on the tasks.
- The file structure contains:
  - Project folder which serves as a main organizer
    - data folder to store data structures to be used
    - src folder to store the source code

## Links

- Official Risk game rules https://www.ultraboardgames.com/risk/game-rules.php
- Game of thrones map https://quartermaester.info/

[Repository](https://github.com/)  
[Trello](https://trello.com/en)
