"""
Copyright @keepbrewing @chibiloveslearning
Basic Code For Pong. 
Some ideas to add or modify:
1) Change the colors
2) Add score and number of lives. If the score becomes 5, the player wins. If number of lives becomes 0, player loses.
3) Show end screen.
4) The speed keeps increasing gradually.
"""
#Import required libraries and modules
import pygame, sys
from pygame import display, event, draw, Rect, mouse

#screen settings - width, height and caption
screen = display.set_mode((600, 600))
display.set_caption("Pong")

#ball initial position and velocities
ballX, ballY = 350, 350
ballSpeed = [0.2,0.3]

#colors
white = (255,255,255)
black = (0,0,0)

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

    #player paddle movement
    paddleY = mouse.get_pos()[1]
    player = Rect(570, paddleY, 20, 100)
    draw.rect(screen, white, player)

    #computer paddle movement
    compY = ballY - 20
    computer = Rect(20, compY, 20, 100)
    draw.rect(screen, white, computer)

    #collision detection
    if(Rect.colliderect(player, ball) or Rect.colliderect(computer, ball)):
        ballSpeed[0] *= -1

    #ball control
    if(ballY < 0 or ballY > 600):
        ballSpeed[1] *= -1
    if(ballX < 0 or ballX > 600):
        ballX, ballY = 350, 350

    #update the screen
    display.flip()

#quit pygame 
pygame.quit()