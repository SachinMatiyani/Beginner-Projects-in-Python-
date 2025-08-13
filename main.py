import pygame
from pygame.locals import *
import random

# Initialize pygame
pygame.init()

# Define some RGB colors
black = (0,0,0)
white = (255,255,255)   
green = (41,240,26)
red = (201, 18, 18)
blue = (50, 153, 213)
yellow = (239,250,32)

# Game window size
win_width = 600
win_height = 400

# Create game window
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

# Snake size and speed
snake = 10 
snake_speed = 10

# Clock object to control game speed
clock = pygame.time.Clock()

# Fonts for text display
font_style = pygame.font.SysFont("bahnschrift", 25)
score_fonts = pygame.font.SysFont("comicsansms", 25)

# Function to display user score on screen
def user_score(score):
    number = score_fonts.render("Score:"+str(score), True, yellow)
    window.blit(number,[0,0])

# Function to draw the snake on screen
def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window,green,[x[0],x[1],snake,snake])
    
# Function to show a message on the screen
def message(msg,color):
    mssg = font_style.render(msg, True, color)
    window.blit(mssg, [0, win_height/2])        # Center vertically

# Main game loop
def game_loop():
    gameOver = False        # When true the game will stop
    gameClose = False       # When true, the option to restart or quit will appear

    # Snake's starting position (center)
    x1 = win_width/2
    y1 = win_height/2

    # Snake movement change variables (initially zero)
    x1_change = 0
    y1_change = 0

    # Snake length data
    snake_length_list = []      # Position list of all segments of snake
    snake_length = 1            # Starting length
    
    # By generating random food position
    foodx = round(random.randrange(0, win_width-snake)/10.0)*10.0
    foody = round(random.randrange(0, win_height-snake)/10.0)*10.0

    while not gameOver:     # the loop will continue until the game is over

        # If the player loses (collisions occur)
        while gameClose == True:
            window.fill(white)              # Background white
            message('You lost! Press P play again and Q quit the game.',red)        
            user_score(snake_length-1)      # Show Score
            pygame.display.update()

            # Restart or quit the event
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:     # Quit
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_p:     # Play again
                        game_loop()
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True             # pressed the game close button
            if event.type == pygame.KEYDOWN:
                # Arrow keys movement control
                if event.key == pygame.K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake

        # If the snake touches the wall then the game closes
        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            gameClose = True

        # By updating the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Background fill
        window.fill(black)

        # Draw food
        pygame.draw.rect(window,red,[foodx,foody,snake,snake])

        # Add a new segment of Snake
        snake_size = []
        snake_size.append(x1)      
        snake_size.append(y1)
        snake_length_list.append(snake_size)

        # If the length limit is crossed then delete the old segment
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]
        
        # Draw snake
        game_snake(snake, snake_length_list)

        # Display Score
        user_score(snake_length-1)

        # Display update
        pygame.display.update()

        # If the snake's head touches the food
        if x1 == foodx and y1 == foody:

            # Generate new food positions
            foodx = round(random.randrange(0, win_width - snake)/10.0)*10.0
            foody = round(random.randrange(0, win_height - snake)/10.0)*10.0
            snake_length +=1    #increase the length of the snake

        
        # Speed control
        clock.tick(snake_speed)
    pygame.quit()   # Off the pygame
    quit()          # Close the pygame

# Start the game
game_loop()