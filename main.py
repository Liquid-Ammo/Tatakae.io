import pygame
from Attack import Moves

pygame.init()
clock = pygame.time.Clock()

testmove = "Infinite Tsukuyomi"


class attack:

  def __init__(self, user, name, hp_oppo, hp_self, ch_oppo, ch_self, velo,
               spread):
    if user == 1:
      self.x = player1.x
      self.y = player1.y
      self.velo = velo
    else:
      self.x = player2.x
      self.y = player2.y
      self.velo = -velo
    self.attack_name = name
    self.hp_oppo = hp_oppo
    self.hp_self = hp_self
    self.ch_oppo = ch_oppo
    self.ch_self = ch_self
    self.spread = spread

  def draw(self):
    pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.spread)


class player:

  def __init__(self, x, y, width, height, color):
    self.x = x
    self.y = y
    self.w = width
    self.h = height
    self.color = color
    self.vel = 20
    self.jump = False
    self.duck = False
    self.jumpCount = 0
    self.duckCount = 0
    self.hp = 1000
    self.ck = 1500
    self.moves = []

  def damage(self, damage):
    self.hp -= damage

  def losechakara(self, damage):
    self.ck -= damage

  def draw(self):
    pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

  def ducknow(self):
    if self.duck:
      if self.duckCount < 7:
        self.y += self.vel
        self.h -= 20
        self.duckCount += 1

      elif self.duckCount < 11:
        self.duckCount += 1

      elif self.duckCount < 18:
        self.y -= self.vel
        self.h += 20
        self.duckCount += 1

      else:
        self.duckCount = 0
        self.duck = False

  def jumpnow(self):
    if self.jump:
      if self.jumpCount < 7:
        self.y -= self.vel
        self.h -= 10
        self.jumpCount += 1
      elif self.jumpCount < 12:
        self.jumpCount += 1
      elif self.jumpCount < 19:
        self.y += self.vel
        self.h += 10
        self.jumpCount += 1
      else:
        self.jumpCount = 0
        self.jump = False


player2 = player(1130, 360, 50, 280, (255, 0, 0))
player1 = player(100, 360, 50, 280, (255, 0, 0))

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tatakae.io")
bg = pygame.image.load("graph.jpg")
bg = pygame.transform.scale(bg, (width, height))

run = True

while run:
  screen.fill((0, 0, 0))
  screen.blit(bg, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  key = pygame.key.get_pressed()

  if key[pygame.K_v]:
    if (not player1.duck) and (not player1.jump):
      player1.jump = True
  player1.jumpnow()

  if key[pygame.K_n]:
    if (not player2.duck) and (not player2.jump):
      player2.jump = True
  player2.jumpnow()

  if key[pygame.K_m]:
    if (not player2.duck) and (not player2.jump):
      player2.duck = True
  player2.ducknow()

  if key[pygame.K_c]:
    if (not player1.duck) and (not player1.jump):
      player1.duck = True
  player1.ducknow()

  for i in player1.moves:
    if i.x < 1280:
      i.x += i.velo
      i.draw()
    else:
      player1.moves.pop(player1.moves.index(i))

  for i in player2.moves:
    if i.x > 0:
      i.x += i.velo
      i.draw()
    else:
      player2.moves.pop(player2.moves.index(i))

  if key[pygame.K_f]:
    if len(player1.moves) < 5:
      player1.moves.append(
          attack(1, testmove, Moves[testmove][0], Moves[testmove][1],
                 Moves[testmove][2], Moves[testmove][3], Moves[testmove][6],
                 Moves[testmove][7]))

  if key[pygame.K_j]:
    if len(player2.moves) < 5:
      player2.moves.append(
          attack(2, testmove, Moves[testmove][0], Moves[testmove][1],
                 Moves[testmove][2], Moves[testmove][3], Moves[testmove][6],
                 Moves[testmove][7]))
  player2.draw()
  player1.draw()

  pygame.display.update()
  clock.tick(60)

pygame.quit()
