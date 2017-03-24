import pygame
import time
import random

pygame.init()

# choose color
white = (255, 255, 255)
green = (51, 153, 51)
black = (0, 0, 0)
red = (255, 0, 0)

# define window size
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))  # display size
pygame.display.set_caption('Project_01')  # Project name / title

img = pygame.image.load('head.png')

# set up clock speed
clock = pygame.time.Clock()

# defining blocksize
blocksize = 20
FPS = 30

direction = "right"
# defining font
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 70)

#defining game intro
def gameIntro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to snakeWorld", green, -100, "large")
        message_to_screen("Eat the red dots by pressing the direction keys", black, -40, "small")
        message_to_screen("press P to play", red, 50, "med")
        pygame.display.update()
        clock.tick(15)

# defing a method,, shows some text while needed
def snake(blocksize, snakelist):
    if direction == 'right':
        head = pygame.transform.rotate(img,270)
    if direction == 'left':
        head = pygame.transform.rotate(img,90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img,180)

    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], blocksize, blocksize])

def text_object(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "med":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface,textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size= 'small'):
    textSurf, textRect = text_object(msg,color,size)
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction
    gameOver = False
    exitGame = False
    # snake position
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0
    # snake extension
    snakelist = []
    snakeLength = 1

    # apple position
    randAppleX = round(random.randrange(0, display_width - blocksize))  # /10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - blocksize))  # /10.0)*10.0

    while not exitGame:
        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game Over", green, -50, size='large')
            message_to_screen("Press C to play again, Q to quit",white,10,size='med')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                    gameOver = True
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exitGame = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame = True
            # print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction="left"
                    lead_x_change = -blocksize
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction="right"
                    lead_x_change = blocksize
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction="up"
                    lead_x_change = 0
                    lead_y_change = -blocksize
                elif event.key == pygame.K_DOWN:
                    direction="down"
                    lead_x_change = 0
                    lead_y_change = blocksize

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        # draw apple
        appleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness, appleThickness])

        # draw snake
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)

        if len(snakelist) > snakeLength:
            del snakelist[0]

        snake(blocksize, snakelist)
        pygame.display.update()

        # apple position

        # if lead_x >= randAppleX and lead_x <= randAppleX + appleThickness:
        #     if lead_y >= randAppleY and lead_y <= randAppleY + appleThickness:
        #         randAppleX = round(random.randrange(0, display_width - blocksize) / 10.0) * 10.0
        #         randAppleY = round(random.randrange(0, display_height - blocksize) / 10.0) * 10.0
        #         snakeLength += 1
        if lead_x > randAppleX and lead_x < randAppleX+appleThickness or lead_x + blocksize > randAppleX and lead_x+blocksize<randAppleX+appleThickness:
            if lead_y > randAppleY and lead_y< randAppleY+appleThickness:
                randAppleX = round(random.randrange(0, display_width - blocksize) / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - blocksize) / 10.0) * 10.0
                snakeLength += 1
            elif lead_y+blocksize > randAppleY and lead_y+blocksize < randAppleY+appleThickness:
                randAppleX = round(random.randrange(0, display_width - blocksize) / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - blocksize) / 10.0) * 10.0
                snakeLength += 1
        clock.tick(FPS)

    # message_to_screen("You Lose!!!!!!!!!!!!!",red)
    # pygame.display.update()
    # time.sleep(2)    
    pygame.quit()
    quit()

gameIntro()
gameLoop()
