import pygame
from Attack import Moves

pygame.init()
clock = pygame.time.Clock()


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
    self.attackCount = 0
    self.hp = 1000
    self.ck = 1500

  def damage(self, damage):
    self.hp -= damage

  def losechakara(self, damage):
    self.ck -= damage

  def draw(self):
    pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

  def ducknow(self):

    if not self.duck:
      self.duck = True
    if self.duck:
      if self.duckCount < 7:
        self.y += self.vel
        self.w -= 20
        self.duckCount += 1

      elif self.duckCount < 11:
        self.duckCount += 1

      elif self.duckCount < 18:
        self.y -= self.vel
        self.w += 20
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
    if not player1.jump:
      player1.jump = True
  player1.jumpnow()

  if key[pygame.K_n]:
    if not player2.jump:
      player2.jump = True
  player2.jumpnow()

  if key[pygame.K_n]:
    player2.jumpnow()

  if key[pygame.K_m]:
    player2.ducknow()

  player2.draw()
  player1.draw()

  pygame.display.update()
  clock.tick(20)

pygame.quit()
