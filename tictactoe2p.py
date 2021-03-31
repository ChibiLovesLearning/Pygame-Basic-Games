"""
Copyright @keepbrewing @chibiloveslearning
Basic Code For Tic Tac Toe 2 player. 
Some ideas to add or modify:
1) Change the colors
2) Can you make second player AI? (Hint : Use Minimax algorithm)
"""
#Import required libraries and modules
import pygame, sys
from pygame import display, event, draw
from numpy import zeros

#screen settings - width, height and caption
screen = display.set_mode((600,600))
display.set_caption("Tic Tac Toe 2 player")

#colors
white = (255,255,255)

#draw the board
square_gap = 600 / 3
draw.line(screen, white, (0, square_gap), (600, square_gap), 10)
draw.line(screen, white, (0, square_gap*2), (600, square_gap*2), 10)
draw.line(screen, white, (square_gap, 0), (square_gap, 600), 10)
draw.line(screen, white, (square_gap*2, 0), (square_gap*2, 600), 10)

#set up variables
game_board = zeros((3,3))
player = 1
game_over = False

#draw X or O
def draw_xo():
    for row in range(0,3):
        for col in range(0,3):
            if game_board[row][col] == 1:
                x = int(col*square_gap + square_gap/2)
                y = int(row*square_gap + square_gap/2)
                draw.circle(screen, white, (x,y), 60, 10)
            if game_board[row][col] == 2:
                draw.line(screen, white, (col*square_gap + 40, row*square_gap+square_gap-50), (col*square_gap+square_gap-50, row*square_gap+40), 10)
                draw.line(screen, white, (col*square_gap + 40, row*square_gap+40), (col*square_gap+square_gap-50, row*square_gap+square_gap-50), 10)


#draw vertical line
def vertical_win(col):
    posX = col*square_gap + square_gap/2
    draw.line(screen, white, (posX, 10) , (posX, 580), 10)

#draw horizontal line
def horizontal_win(row):
    posY = row*square_gap + square_gap/2
    draw.line(screen, white, (10, posY), (580, posY), 10)

#draw ascending line
def ascending_win():
    draw.line(screen, white, (10, 580), (580, 10), 10)

#draw descending line
def descending_win():
    draw.line(screen, white, (10, 10), (580, 580), 10)

#check if a player has won
def check_winner(player):
    for col in range(0,3):
        if game_board[0][col] == player and game_board[1][col] == player and game_board[2][col] == player:
            vertical_win(col)
            return True

    for row in range(0,3):
        if game_board[row][0] == player and game_board[row][1] == player and game_board[row][2] == player:
            horizontal_win(row)
            return True

    if game_board[2][0] == player and game_board[1][1] == player and game_board[0][2] == player:
        ascending_win()
        return True

    if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
        descending_win()
        return True

    return False

#game loop
while True:
    events = event.get()
    for e in events:
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN and not game_over:
            #get mouse coordinates
            mouseX, mouseY = e.pos
            #which square was clicked
            clicked_row = int(mouseY / square_gap)
            clicked_col = int(mouseX / square_gap)
            #if a square is available
            if game_board[clicked_row][clicked_col] == 0:
                if player == 1:
                    game_board[clicked_row][clicked_col] = 1
                    if check_winner(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    game_board[clicked_row][clicked_col] = 2
                    if check_winner(player):
                        game_over = True
                    player = 1
                draw_xo()
    
    #update screen
    display.flip()

#quit pygame
pygame.quit()