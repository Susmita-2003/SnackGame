# tut3---------------------------------

import pygame
X = pygame.init()

# creating window
gameWindow = pygame.display.set_mode((1200, 600))
# tut4---------------------------------
pygame.display.set_caption("My First Game")

# game specific variables
exit_games = False
game_over = False

# tut5---------------------------------
# creating game loop
while not exit_games:
   for event in pygame.event.get():                          # tut6---------------------------------
      print(event)

pygame.quit()
quit()

# tut6---------------------------------