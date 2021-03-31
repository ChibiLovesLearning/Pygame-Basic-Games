"""
Copyright @keepbrewing @chibiloveslearning
Basic Code For Hangman. 
"""
import pygame, sys, random
from pygame import display, event, font

pygame.init()
screen = display.set_mode((800, 600))
display.set_caption("Hangman")

#colors
white = (255,255,255)
black = (0,0,0)

title = font.Font("freesansbold.ttf", 60)
titleText = title.render("HANGMAN", True, white)

wordFont = font.Font("freesansbold.ttf", 40)

words = ["peanut", "mustard", "almond", "ketchup", "pistachio"]
word = random.choice(words)
guessed_letters = []
no_of_tries = 5
game_over = False

while True:
    events = event.get()
    for e in events:
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN and not game_over:
            ch = e.unicode
            if ch in word:
                guessed_letters.append(ch)
            if ch not in word:
                no_of_tries -= 1

    screen.fill(black)
    screen.blit(titleText, (220, 150))

    display_word = ""
    for char in word:
        if char in guessed_letters:
            display_word += char + " "
        if char not in guessed_letters:
            display_word += " _ "
    wordText = wordFont.render(display_word, True, white)
    screen.blit(wordText, (220, 250))

    triesFont = wordFont.render("Tries : " + str(no_of_tries), True, white)
    screen.blit(triesFont, (100, 400))

    if(no_of_tries == 0):
        game_over = True
        message = wordFont.render("You LOSE!", True, white)
        screen.blit(message, (500, 400))

    won = True
    for c in word:
        if c not in guessed_letters:
            won = False

    if(won):
        game_over = True
        message = wordFont.render("You WIN!", True, white)
        screen.blit(message, (500, 400))

    display.flip()

pygame.quit()