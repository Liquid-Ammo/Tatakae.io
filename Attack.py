import pygame
from subprocess import call  # for clear
import os  # for clear
from time import sleep  # for time delay



# to clear the screen
def clear():
  _ = call("clear" if os.name == "posix" else "cls")


clear()

# damage oppo ,damage self , chakara oppo, chakara self, afterblock oppo, afterblock self


# Changed Move Names
Moves = {
    "Berserker Barrage": [-500, -100, 0, -200, 0, 0],  # 1
    "Deadly Chop": [-150, 0, 0, 0, 0, 0],  # 2
    "Tempest Thrust": [-200, 0, 0, -100, -100, 0],  # 3
    "Flame Breath": [-250, 0, 0, -200, 0, -200],  # 4
    "Earth Shield": ["-50", +200, 0, -100, 0, 0],  # 5
    "Tidal Takedown": ["-250", 0, 0, -100, 0, 0],  # 6
    "Unwavering Will": [0, -150, 0, +300, 0, 0],  # 7
    "Eye Gouge": ["100", 0, 0, 0, 0, 0],  # 8
    "Life Drain": [-100, 0, -200, -200, 0, 0],  # 9
    "Gods Grace": [0, +150, 0, +150, 0, 0],  # 10
    "Aura of Restoration": [0, +400, 0, -300, 0, 0],  # 11
    "Skyward Leap": [0, 0, 0, -50, 0, 0],  # 12
    None: [0, 0, 0, 10, 0, 0]  # 13
}

# Move clasification
attack = [
    "Berserker Barrage",
    "Deadly Chop",
    "Tempest Thrust",
    "Flame Breath",
    "Tidal Takedown",
    "Eye Gouge"
]
defence = ["Earth Shield", "Aura of Restoration", "Gods Grace"]
filler = ["Unwavering Will", "Skyward Leap", "Life Drain", None]

# initial strength
