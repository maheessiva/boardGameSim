# Maheeshan Sivanesan 101271048 
# 2022-11-04 
# COMP 1405 - Assignment 06

# to import the functions from the pygame library
import pygame
import random

# to keep track of the square that p1 and p2 is at
p1_pos = 0
p2_pos = 0

# to initialize font for numbered tiles feature
pygame.init()

# to create a surface that is 700x600 to draw on
drawing_window = pygame.display.set_mode((700, 600))

# to fill the surface with the colour white
drawing_window.fill((255, 255, 255))

# to keep track of the colour of the squares
counter = 0

# set the font to be used for numbering the tiles
font = pygame.font.SysFont('Calibri', 25)

# The following nested for loop constructs the game board with numbered tiles
# go through each row
for y in range(6):
    # go through each column in each row
    for x in range(7):
        if (counter%2 == 0):
            pygame.draw.rect(drawing_window, (255,0,0), (((x*100), (y*100)), (100, 100)))
        counter = counter + 1
        # to add the numbers to the tiles
        text = font.render(str(counter), True, (0,0,0))
        # to create a rectangular object for the numbers
        textRect = text.get_rect()
        # to set the center of the rectangular object
        textRect.center = ((x*100)+50, (y*100)+50)
        drawing_window.blit(text, textRect)

# to initialize p1 and p2 positions and then draw their tokens
p1pos_x = 50
p1pos_y = 20
p2pos_x = 50
p2pos_y = 80
pygame.draw.circle(drawing_window, (0,255,0), (p1pos_x,p1pos_y), 10)
pygame.draw.circle(drawing_window, (0,0,255), (p2pos_x,p2pos_y), 10)
# update display after drawing is complete
pygame.display.update()
pygame.time.delay(2000)

# to keep track of p1 and p2 turns
p1turn = True

# while p1 and p2 haven't reached the end of the board
while((p1_pos<41) and (p2_pos<41)):
    # to store location of p1 and p2 after each turn
    x_pos = 0
    y_pos = 0
    # For player 1's turn:
    if(p1turn):
        # roll 2 6-sided dice and add and print the value
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1+die2
        print("Player 1 rolled a", die1, "and", die2, "for a total of", total, "moves")
        # add total squares moved to p1 position so they move from that spot next time
        p1_pos += total
        # Counter to keep track of red and white squares
        counter = 0
        # To keep track of number of moves after dice is rolled
        moves = 0
        # To end p1's turn after done moving
        p1done = False
        # The following nested for loop moves p1's green token for each move
        # go through each row
        for y in range(6):
            # if p1 is done moving their token, break
            if(p1done):
                break
            # go through each column in each row
            for x in range(7):
                # to set x and y location of p1 token
                p1pos_x = (x*100)+50
                p1pos_y = (y*100)+20
                # if counter is even, draw red square, else draw white square
                if (counter%2 == 0):
                    pygame.draw.rect(drawing_window, (255,0,0), (((x*100), (y*100)), (100, 100)))
                else:
                    pygame.draw.rect(drawing_window, (255,255,255), (((x*100), (y*100)), (100, 100)))
                counter = counter + 1
                # re-draw the squares and numbers to cover the previous token's location
                text = font.render(str(counter), True, (0,0,0))
                textRect = text.get_rect()
                textRect.center = ((x*100)+50, (y*100)+50)
                drawing_window.blit(text, textRect)
                # after p1 token is at its location, break from the for loop
                if(moves == p1_pos):
                    x_pos = x*100
                    y_pos = y*100
                    p1done = True
                    break
                moves = moves+1
        # draw p1 and p2 tokens and then update screen
        pygame.draw.circle(drawing_window, (0,255,0), (p1pos_x,p1pos_y), 10)
        pygame.draw.circle(drawing_window, (0,0,255), (p2pos_x,p2pos_y), 10)
        pygame.display.update()
        pygame.time.delay(2000)
        # implementation of "sorry collisions" feature
        # if p1 lands on p2's square, send p2 back to start
        if(p1_pos==p2_pos):
            pygame.draw.circle(drawing_window, (0,0,255), (50,80), 10)
            p2_pos=0
            if (counter%2 == 0):
                pygame.draw.rect(drawing_window, (255,255,255), (((x_pos), (y_pos)), (100, 100)))
            else:
                pygame.draw.rect(drawing_window, (255,0,0), (((x_pos), (y_pos)), (100, 100)))
            text = font.render(str(counter), True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (x_pos+50, y_pos+50)
            drawing_window.blit(text, textRect)
            pygame.draw.circle(drawing_window, (0,255,0), (p1pos_x,p1pos_y), 10)
            print("Player 1 lands on Player 2, so Player 2 goes back to the start!")
            pygame.display.update()
            pygame.time.delay(2000)
        p1turn = False
    
    # For player 2's turn:
    if((p1turn == False) and (p1_pos<41)):
        # roll 2 6-sided dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1+die2
        p2_pos += total
        print("Player 2 rolled a", die1, "and", die2, "for a total of", total, "moves")
        counter = 0
        moves = 0
        p2done = False
        # go through each row
        for y in range(6):
            if(p2done):
                break
            # go through each column in each row
            for x in range(7):
                p2pos_x = (x*100)+50
                p2pos_y = (y*100)+80
                if (counter%2 == 0):
                    pygame.draw.rect(drawing_window, (255,0,0), (((x*100), (y*100)), (100, 100)))
                else:
                    pygame.draw.rect(drawing_window, (255,255,255), (((x*100), (y*100)), (100, 100)))
                counter = counter + 1
                text = font.render(str(counter), True, (0,0,0))
                textRect = text.get_rect()
                textRect.center = ((x*100)+50, (y*100)+50)
                drawing_window.blit(text, textRect)
                if(moves == p2_pos):
                    x_pos = x*100
                    y_pos = y*100
                    p2done = True
                    break
                moves = moves+1
        pygame.draw.circle(drawing_window, (0,0,255), (p2pos_x,p2pos_y), 10)
        pygame.draw.circle(drawing_window, (0,255,0), (p1pos_x,p1pos_y), 10)
        pygame.display.update()
        pygame.time.delay(2000)
        if(p1_pos==p2_pos):
            pygame.draw.circle(drawing_window, (0,255,0), (50,20), 10)
            p1_pos=0
            if (counter%2 == 0):
                pygame.draw.rect(drawing_window, (255,255,255), (((x_pos), (y_pos)), (100, 100)))
            else:
                pygame.draw.rect(drawing_window, (255,0,0), (((x_pos), (y_pos)), (100, 100)))
            text = font.render(str(counter), True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (x_pos+50, y_pos+50)
            drawing_window.blit(text, textRect)
            pygame.draw.circle(drawing_window, (0,0,255), (p2pos_x,p2pos_y), 10)
            print("Player 2 lands on Player 1, so Player 1 goes back to the start!")
            pygame.display.update()
            pygame.time.delay(2000)
        p1turn = True
    # whoever reaches the end of the board first wins
    if(p1_pos>=41):
        print("Player 1 wins!")
    elif(p2_pos>=41):
        print("Player 2 wins!")
            
            
# allows user to close the surface
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()