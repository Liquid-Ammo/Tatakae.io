# modules
import pygame
from subprocess import call  # for clear
import os  # for clear
from time import sleep  # for time delay


# to clear the screen
def clear():
  _ = call("clear" if os.name == "posix" else "cls")


clear()
'''

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
    None: [0, 0, 0, 10, 0, 0],  # 13
}

# Move clasification
attack = [
    "Berserker Barrage",
    "Deadly Chop",
    "Tempest Thrust",
    "Flame Breath",
    "Tidal Takedown",
    "Eye Gouge",
]
defence = ["Earth Shield", "Aura of Restoration", "Gods Grace"]
filler = ["Unwavering Will", "Skyward Leap", "Life Drain", None]

# initial strength

p1_hp = 1000
p2_hp = 1000
p1_ck = 1500
p2_ck = 1500

# 6 by 10 matrix for the game back bone
a0 = [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "]
a1 = [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "]
a2 = [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "]
a3 = ["O", 0, 0, 0, 0, 0, 0, 0, 0, "O"]
a4 = ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"]
a5 = ["^", 0, 0, 0, 0, 0, 0, 0, 0, "^"]
print(a1, a2, a3, a4, a5, sep="\n")

# functions


# jumping
def jump(c=1):
    n = 10
    if c == 1:
        n = 0
    if c == 2:
        n = 9
    sleep(0.3)
    clear()
    for i in range(2):
        print(a1, a2, a3, a4, a5, sep="\n")
        a1[n] = a2[n]
        a2[n] = a3[n]
        a3[n] = a4[n]
        a4[n] = a5[n]
        a5[n] = a0[n]
        sleep(0.1)
        print()
        clear()
    for i in range(2):
        print(a1, a2, a3, a4, a5, sep="\n")
        a5[n] = a4[n]
        a4[n] = a3[n]
        a3[n] = a2[n]
        a2[n] = a1[n]
        a1[n] = a0[n]
        sleep(0.1)
        print()
        clear()
    print(a1, a2, a3, a4, a5, sep="\n")


# ducking
def duck(c):
    n = 4
    if c == 1:
        n = 0
    if c == 2:
        n = 9
    sleep(0.3)
    clear()
    if True:
        print(a1, a2, a3, a4, a5, sep="\n")
        a0[n] = a4[n]
        a4[n] = a3[n]
        a3[n] = a2[n]
        sleep(0.25)
        print()
        clear()
    if True:
        print(a1, a2, a3, a4, a5, sep="\n")
        a3[n] = a4[n]
        a4[n] = a0[n]
        a0[n] = a1[n]
        sleep(0.25)
        print()
        clear()
    print(a1, a2, a3, a4, a5, sep="\n")


# inputs for now will be part of pygame later
for i in range(0, 4):
    a = int(input("jump : "))
    jump(a)
    b = int(input("Duck : "))
    duck(b)
'''
# under test do not edit the code below "the commented one"

# pygame init
pygame.init()
# screen
screen = pygame.display.set_mode((1080, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Tatakae.io")
player1 = pygame.Rect((0, 0, 50, 50))
player2 = pygame.Rect((70, 0, 50, 50))
run = True

bg_image = pygame.image.load("bg.jpg").convert_alpha()


def draw_bg():
  bg_ima = pygame.transform.scale(bg_image, (1080, 600))
  screen.blit(bg_ima, (0, 0))


while run:
  pygame.draw.rect(screen, (0, 0, 255), player1)
  pygame.draw.rect(screen, (255, 0, 0), player2)
  draw_bg()
  for event in pygame.event.get():
    key = pygame.key.get_pressed()
    if event.type == pygame.QUIT:
      run = False
    if key[pygame.K_a]:
      player1.x -= 1
    if key[pygame.K_d]:
      player1.x += 1
    if key[pygame.K_w]:
      player1.y -= 1
    if key[pygame.K_s]:
      player1.y += 1

    if key[pygame.K_h]:
      player2.x -= 1
    if key[pygame.K_k]:
      player2.x += 1
    if key[pygame.K_u]:
      player2.y -= 1
    if key[pygame.K_j]:
      player2.y += 1
  pygame.display.update()
  clock.tick(120)
pygame.quit()
