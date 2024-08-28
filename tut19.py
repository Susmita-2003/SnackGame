# start snack game

import pygame
import random
import os


pygame.mixer.init()   #this is for adding music 

# pygame initialization
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


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)


def text_screen(text, color, x, y):
    screen_text = font.render(text,  True, color)
    gameWindow.blit(screen_text, [x,y])



def plot_snack(gameWindow, color, snk_list, snack_size):
    for x,y in snk_list:
    #   print(snk_list)
      pygame.draw.rect(gameWindow, color, [x, y, snack_size, snack_size])

def welcome_screen():
    exit_game = False
    while not exit_game:
        gameWindow.fill((150, 110, 210))     # To change color try diffrent set of number between(0 - 255)
        text_screen("--- Welcome To Snack Game ---", black, 400, 200)
        text_screen("Khelna hai to spacebar key press kro", black, 350, 260)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('Livin_Up.mp3')
                    pygame.mixer.music.play()
                    game_loop()    


        pygame.display.update()
        clock.tick(60)


# creating game loop
def game_loop():
    
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
    snk_list = []
    snk_lenth = 1
    score = 0
    fps = 40                 #maintence the speed of snack
    init_valocity = 5        #maintence the speed of snack
    

    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    

    while not exit_games:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(white)
            text_screen("heyy Mar gya saanp! Chal Enter dbaa firse khelna hai To..", red, 250, 250)
        
            for event in pygame.event.get(): 
                # print(event)                         
                    if event.type == pygame.QUIT:
                        exit_games = True
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            welcome_screen()    #game over if it will touch the wall and after press enter it will restart.


        else:
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

                    if event.key == pygame.K_q:       # Adding Cheatcode by pressing key q score will jump +5
                        score += 5                

                            
            snack_X += velocity_x
            snack_y += velocity_y


            if abs(snack_X - food_X)<10 and abs(snack_y - food_y)<10:    #maintain the overlap of snack on food
                score = score + 5
                # print("score : ", score * 5)
                food_X = random.randint(10, screen_width/2)
                food_y = random.randint(10, screen_hight/2)
                snk_lenth += 4   #we are increasing coordinate
                if score > int(hiscore):
                    hiscore = score
            
            
            gameWindow.fill(white)
            text_screen("score: "+ str(score) + "  Hiscore : "+ str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_X, food_y, snack_size, snack_size])


            head = []
            head.append(snack_X)
            head.append(snack_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenth:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameOver.mp3')
                pygame.mixer.music.play()


            if snack_X < 0 or snack_X > screen_width or snack_y < 0 or snack_y > screen_hight:
                game_over = True
                pygame.mixer.music.load('gameOver.mp3')
                pygame.mixer.music.play()

                # print("game_over")

            # pygame.draw.rect(gameWindow, black, [snack_X, snack_y, snack_size, snack_size])
            plot_snack(gameWindow, black, snk_list, snack_size)

        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()


welcome_screen()
