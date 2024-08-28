# start snack game

import pygame
import random


X = pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


screen_width = 1200
screen_hight = 600

# creating window
gameWindow = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("SnackesWithHarry")
pygame.display.update()

# game specific variables
exit_games = False
game_over = False
snack_X = 45
snack_y = 55
snack_size = 15         #maintence the size of snack
velocity_x = 0
velocity_y = 0
food_X = random.randint(10, screen_width/2)
food_y = random.randint(10, screen_hight/2)
score = 0
clock = pygame.time.Clock()
fps = 40                 #maintence the speed of snack
init_valocity = 5        #maintence the speed of snack

# creating game loop
while not exit_games:
    for event in pygame.event.get(): 
      # print(event)                         
        if event.type == pygame.QUIT:
          exit_games = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x =   init_valocity
                velocity_y = 0
    
            if event.key == pygame.K_LEFT:
                velocity_x =  - init_valocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y  =  - init_valocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y  =  init_valocity
                velocity_x = 0
    
    snack_X += velocity_x
    snack_y += velocity_y


    if abs(snack_X - food_X)<10 and abs(snack_y - food_y)<10:    #maintain the overlap of snack on food
        score = score + 1
        print("score : ", score * 5)
        food_X = random.randint(10, screen_width/2)
        food_y = random.randint(10, screen_hight/2)

    
    
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, red, [food_X, food_y, snack_size, snack_size])
    pygame.draw.rect(gameWindow, black, [snack_X, snack_y, snack_size, snack_size])
    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()


