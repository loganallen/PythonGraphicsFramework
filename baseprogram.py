# Program Base!!!

import pygame
import random
import math
import sys
from pygame.locals import *


# Initialize pygame
pygame.init()

# Create the screen
screen_width = 640
screen_height = 460
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Using Pygame")
main_clock = pygame.time.Clock()


# _________ Instantiate variables here _________ #
##################################################

# Create background color
background_color = (255,255,255)

font1 = pygame.font.SysFont(None,36)

# Player rectangle with movement variables
player = pygame.Rect(150,300,50,50)
player_up = False
player_down = False
player_right = False
player_left = False
player_speed = 4

# Enemy rectangle
enemy = pygame.Rect(400,100,75,75)
enemy_right = True
enemy_left = False
enemy_speed = 3



#  ___________ Create Methods below __________ #
################################################

def draw_text(display_string, font, surface, coordinates, color):
    text_display = font.render(display_string, 1, color)
    surface.blit(text_display, coordinates)


# Infinite Game Loop
while True:

    # _____________ Check for events _____________ #
    ################################################

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Code for keys pressed
        if event.type == KEYDOWN:

            # Change movement variables for player
            if event.key == K_a:
                player_left = True
                player_right = False
            if event.key == K_d:
                player_right = True
                player_left = False
            if event.key == K_w:
                player_up = True
                player_down = False
            if event.key == K_s:
                player_down = True
                player_up = False

        # Code for keys released
        if event.type == KEYUP:

            # Change movements variables for player
            if event.key == K_a:
                player_left = False
            if event.key == K_d:
                player_right = False
            if event.key == K_w:
                player_up = False
            if event.key == K_s:
                player_down = False


    # __________ Begin graphical displays ________ #
    ################################################

    # Set the framerate speed
    main_clock.tick(50)
    # Fill background everytime with background color
    screen.fill(background_color)


    # ____________ Draw objects below ____________ #
    ################################################

    # Draw enemy rectangle with black outline
    pygame.draw.rect(screen,(150,0,0),enemy,0)
    pygame.draw.rect(screen,(0,0,0),enemy,1)

    # Draw player with black outline
    pygame.draw.rect(screen,(0,0,150),player,0)
    pygame.draw.rect(screen,(0,0,0),player,1)

    # Display collision detection
    if player.colliderect(enemy):
        draw_text("Collision!",font1,screen,(30,30),(0,150,0))







    # ___________ Animate objects below __________ #
    ################################################

    # AI movement of enemy back and forth
    if enemy_right:
        enemy.x += enemy_speed
        if enemy.right >= screen_width:
            enemy_right = False
            enemy_left = True
    elif enemy_left:
        enemy.x -= enemy_speed
        if enemy.left <= 0:
            enemy_left = False
            enemy_right = True

    # Move the player within the screen
    if player_right and player.right <= screen_width:
        player.x += player_speed
    elif player_left and player.left >= 0:
        player.x -= player_speed
    if player_up and player.top >= 0:
        player.y -=player_speed
    elif player_down and player.bottom <= screen_height:
        player.y += player_speed






    # Lastly, update the screen
    pygame.display.update()

    