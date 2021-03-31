"""
Copyright @keepbrewing @chibiloveslearning
Basic Code For Squash. 
Some ideas to add or modify:
1) Change the colors
2) Add score and number of lives. If the score becomes 10, the player wins. If number of lives becomes 0, player loses.
3) Show end screen.
"""
#Import required libraries and modules
import pygame, sys
from pygame import display, event, draw, Rect, mouse

#screen settings - width, height and caption
screen = display.set_mode((600, 600))
display.set_caption("Squash")

#colors
white = (255,255,255)
black = (0,0,0)

#ball initial position and velocities
ballX, ballY = 100, 10
ballSpeed = [0.2, 0.2]

#game loop
while True:
    events = event.get()
    for e in events:
        if e.type == pygame.QUIT:
            sys.exit()

    #background
    screen.fill(black)

    #ball movement
    ballX += ballSpeed[0]
    ballY += ballSpeed[1]
    draw.circle(screen, white, (ballX, ballY), 20)
    #getting rectangle of ball
    ball = Rect(ballX, ballY, 20, 20)

    #paddle movement
    paddleX = mouse.get_pos()[0]
    paddle = Rect(paddleX, 550, 100, 20)
    draw.rect(screen, white, paddle)

    #ball control
    if(ballX < 0 or ballX > 600):
        ballSpeed[0] *= -1
    if(ballY < 0 or Rect.colliderect(ball, paddle)):
        ballSpeed[1] *= -1
    if(ballY > 600):
        ballX, ballY = 100, 10

    #update the screen
    display.flip()

#quit pygame 
pygame.quit()