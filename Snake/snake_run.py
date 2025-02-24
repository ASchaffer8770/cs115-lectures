import pygame

#init pygame
pygame.init()

#setup screen
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

#set window title
pygame.display.set_caption("Snake")

#setting fps
clock = pygame.time.Clock()
dt = 0
speed = 10

"""GAME LOOP"""
running = True
while running:
  """Handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  """Update game state"""

  """draw to the screen"""
  #clear screen
  screen.fill("black")

  #update screen
  pygame.display.flip()

  #fps
  dt = clock.tick(speed)/1000


#quit app
pygame.quit()