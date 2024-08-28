# start snack game

import pygame
X = pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# creating window
gameWindow = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("SnackesWithHarry")
pygame.display.update()

# game specific variables
exit_games = False
game_over = False

# creating game loop
while not exit_games:
    for event in pygame.event.get():                          
      if event.type == pygame.QUIT:
        exit_games = True
    
    gameWindow.fill(white)
    pygame.display.update()



pygame.quit()
quit()

# tut7---------------------------------

