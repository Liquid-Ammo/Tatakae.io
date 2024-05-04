# modules
import pygame
from subprocess import call  #for clear
import os  # for clear
from time import sleep  #for time delay


#to clear the screen
def clear():
  _ = call('clear' if os.name == 'posix' else 'cls')


clear()

# under test do not edit the code below "the commented one"
'''
#pygame init
pygame.init()
#screen
screen = pygame.display.set_mode((800, 600))
player1 = pygame.Rect((0, 0, 50, 50))
player2 = pygame.Rect((70, 0, 50, 50))
run = True

while run:

  pygame.draw.rect(screen, (0, 0, 255), player1)
  pygame.draw.rect(screen, (255, 0, 0), player2)

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

pygame.quit()
'''


# damage oppo ,damage self , chakara oppo, chakara self, afterblock oppo, afterblock self

jutsu = {
    "Rinnegan": [-100000000, 0, 0, 0, 0, 0],  # 1
    "Chidori": [-200, 0, 0, -50, 0, 0],  # 2
    "Rasengan": [-100, 0, 0, -50, -50, 0],  # 3
    "Fire": [-300, 0, 0, -200, 0, -200],  # 4
    "Earth": ["-10", 0, 0, -50, 0, 0],  # 5
    "Water": ["-100", 0, 0, -300, 0, 0],  # 6
    "Byakugan": [0, 0, 0, -200, 0, 0],  # 7
    "Magekyo": ["50", 0, 0, -300, 0, 0],  # 8
    "Izanagi": [0, "100", 0, -200, 0, 0],  # 9
    "Ninja": [0, +100, 0, -100, 0, 0],  # 10
    "Seventh": [0, -500, 0, +700, 0, 0],  # 11
    "Jump": [0, 0, 0, -50, 0, 0],  #12
    None: [0, 0, 0, 10, 0, 0]  #13
}

# jutsu clasification
attack = ["Rinnegan", "Chidori", "Rasengan", "Fire"]
defence = ["Earth", "Water", "Jump", "Magekyo"]
filler = ["Ninja", "Seventh", "Izanagi", None]

# initial strength

p1_hp = 1000
p2_hp = 1000
p1_ck = 1500
p2_ck = 1500

#6 by 10 matrix for the game back bone
a0 = [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "]
a1 = [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "]
a2 = [" ", 0, 0, 0, 0, 0, 0, 0, 0, " "]
a3 = ["O", 0, 0, 0, 0, 0, 0, 0, 0, "O"]
a4 = ["|", 0, 0, 0, 0, 0, 0, 0, 0, "|"]
a5 = ["^", 0, 0, 0, 0, 0, 0, 0, 0, "^"]
print(a1, a2, a3, a4, a5, sep="\n")

#functions


#jumping
def jump(c=1):
  n = 4
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


#ducking
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


#inputs for now will be part of pygame later
while True:
  a = int(input("jump : "))
  jump(a)
  b = int(input("Duck : "))
  duck(b)
#Lalith