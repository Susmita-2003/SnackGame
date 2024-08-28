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
snack_X = 45
snack_y = 55
snack_size = 10
velocity_x = 10
velocity_y = 10
clock = pygame.time.Clock()
fps = 30


# creating game loop
while not exit_games:
    for event in pygame.event.get(): 
      # print(event)                         
        if event.type == pygame.QUIT:
          exit_games = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snack_X = snack_X + 10
    
            if event.key == pygame.K_LEFT:
                snack_X = snack_X - 10

            if event.key == pygame.K_UP:
                snack_y = snack_y - 10

            if event.key == pygame.K_DOWN:
                snack_y = snack_y + 10
    
    snack_X += velocity_x
    snack_y += velocity_y

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snack_X, snack_y, snack_size, snack_size])
    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()


