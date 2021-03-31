"""
Copyright @keepbrewing @chibiloveslearning
Basic Code For Drawing Pad. 
Some ideas to add or modify:
1) Change the colors
2) Add three buttons for three different colors that the user can choose on click.
3) Add an eraser.
"""
#Import required libraries and modules
import pygame, sys, random
from pygame import display, event, mouse, draw

#screen settings - width, height and caption
screen = display.set_mode((600,600))
display.set_caption("Drawing Pad")

#colors
white = (255,255,255)

#game loop
while True:
    events = event.get()
    for e in events:
        if e.type == pygame.QUIT:
            sys.exit()

    #get mouse coordinates
    x, y = mouse.get_pos()
    #returns True if left button is pressed
    left_button = mouse.get_pressed()[0]
    #random RGB colors
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    #if left button is pressed, then draw circle
    if(left_button):
        draw.circle(screen, color, (x,y), 10)
    
    #update the screen
    display.flip()

#quit pygame 
pygame.quit()