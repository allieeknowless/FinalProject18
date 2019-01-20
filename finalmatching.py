import pygame ##import pygame module
import time ##imports time
import random  ##imports random
from random import shuffle ##Used to randomly shuffle the board each round


choice1 = 1 #will change during loop
choice2 = 2 #will change during loop

pygame.init() #initializes pygame's submodules
screen = pygame.display.set_mode((418, 490)) ##sets the screen size
running = True ## to control while loop


my_font = pygame.font.SysFont("Arial", 48) #set the font for the title
my_font2 = pygame.font.SysFont("Arial", 28) #sets font for the grid labels
my_font3 = pygame.font.SysFont("Arial", 60) #sets a different sized font

#there are 16 boxes, so there are 8 colors and 2 of each
color1 = (255, 0, 0)
color2 = (255, 0, 0)
color3 = (0, 0, 255)
color4 = (0, 0, 255)
color5 = (0, 255, 0)
color6 = (0, 255, 0)
color7 = (255, 255, 0)
color8 = (255, 255, 0)
color9 = (255, 100, 180)
color10 = (255,100,180)
color11 = (115, 0, 0)
color12 = (115, 0, 0)
color13 = (190, 0, 255)
color14 = (190, 0, 255)
color15 = (200,200,200)
color16 = (200,200,200)
color_choices = [(color1), (color2), (color3), (color4), (color5), (color6), (color7), (color8), (color9), (color10), (color11), (color12),
 (color13), (color14), (color15), (color16)] #list of all colors to choose from
random.shuffle(color_choices) ##randomly shuffles the board each round

##dimensions of all 16 boxes
BOX1 = [5, 5, 100, 100] 
BOX2 = [108, 5, 100, 100]
BOX3 = [211, 5, 100, 100]
BOX4 = [314, 5, 100, 100]
BOX5 = [5, 108, 100, 100]
BOX6 = [108, 108, 100, 100]
BOX7 = [211, 108, 100, 100]
BOX8 = [314, 108, 100, 100]
BOX9 = [5, 211, 100, 100]
BOX10 = [108, 211, 100, 100]
BOX11 = [211, 211, 100, 100]
BOX12 = [314, 211, 100, 100]
BOX13 = [5, 314, 100, 100]
BOX14 = [108, 314, 100, 100]
BOX15 = [211, 314, 100, 100]
BOX16 = [314, 314, 100, 100]



#numbered labels for all 16 boxes
text1 = my_font.render("1", True, (255, 255, 255))
text2 = my_font.render("2", True, (255, 255, 255))
text3 = my_font.render("3", True, (255, 255, 255))
text4 = my_font.render("4", True, (255, 255, 255))
text5 = my_font.render("5", True, (255, 255, 255))
text6 = my_font.render("6", True, (255, 255, 255))
text7 = my_font.render("7", True, (255, 255, 255))
text8 = my_font.render("8", True, (255, 255, 255))
text9 = my_font.render("9", True, (255, 255, 255))
text10 = my_font.render("10", True, (255, 255, 255))
text11 = my_font.render("11", True, (255, 255, 255))
text12 = my_font.render("12", True, (255, 255, 255))
text13 = my_font.render("13", True, (255, 255, 255))
text14 = my_font.render("14", True, (255, 255, 255))
text15 = my_font.render("15", True, (255, 255, 255))
text16 = my_font.render("16", True, (255, 255, 255))
##labels for other buttons/messages
text_restart = my_font2.render("restart", True, (255, 255, 255))
text_lose = my_font3.render("YOU LOSE :(", True, (20, 118, 19))
text_win= my_font3.render("YOU WIN!!!!!", True, (200, 118, 255))

##keeps track of when it is an even round 
even = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]

turns = 40 ##ypu get a total of 20 guesses, which is 40 clicks

class round:
        """keeps track of matches"""
        def __init__(self,matches):
                self.matches = matches

        def increase_matches(self):
                self.matches += 1 ##matches increases by 1

round1 = round(0) ##round starts with 0 matches

def update():
        """updates the screen after a wrong choice, so the colors light up then disappear"""
        pygame.display.flip() ##update the display
        grid() 
        pygame.time.wait(500) ###keep the colors visible for 500 milliseconds
        pygame.draw.rect(screen, (0,0,0), box_choice1) ##then make the colors disappear
        pygame.draw.rect(screen, (0,0,0), box_choice2) ##then make the colors disappear
        

def check_match():
        '''checks to see if a match has been made'''
        global turns 
        if turns <= 0: ##if there are no turns left
                if choice1 == choice2: ## but the last choice was a match
                        round1.increase_matches() ##increase match by 1
                        if round1.matches == 8: ##if all matches have been made
                                print ("WINNNER")
                                win() ##show winning screen
                        else:##if not all matches have been made
                                print("LOSER")
                                lose()    ###show losing screen  
                else:
                        print("LOSER")
                        lose() ##show losing screen if there are no moves left, and the last move was not a match
        else:
                if box_choice1 == box_choice2: ##if user clicks the same button twice
                        print (f"Don't click on the same box twice, {turns} clicks left.")
                        update()
                elif choice1 == choice2: ##if the two colors match
                        round1.increase_matches() ##increase match by 1
                        if round1.matches == 8: ##and if all matches have been made
                                print ("WINNNER")
                                win() #show winning screen
                        else: ##not all matches have been made
                                print(f"match, {turns} clicks left") ##keep the colors there and print 'match'
                else:##if the two colors do not match
                                print(f"no match, {turns} clicks left") ## print 'no'
                                print(round1.matches)
                                update()

def lose():
        """losing screen"""
        pygame.draw.rect(screen, (255,255,255), (65, 160, 300, 100))
        screen.blit(text_lose, (65, 170))

def win():
        """winning scree"""
        pygame.draw.rect(screen, (255,255,255), (65, 160, 300, 100))
        screen.blit(text_win, (70, 170))


def grid():
        '''creates a numbered grid of 16 rectangles''' 
        ###draw sixteen white rectangles of the same size in specified locations
        pygame.draw.rect(screen, (255,255,255), BOX1, 1)
        pygame.draw.rect(screen, (255,255,255), BOX2, 1)
        pygame.draw.rect(screen, (255,255,255), BOX3, 1)
        pygame.draw.rect(screen, (255,255,255), BOX4, 1)
        pygame.draw.rect(screen, (255,255,255), BOX5, 1)
        pygame.draw.rect(screen, (255,255,255), BOX6, 1)
        pygame.draw.rect(screen, (255,255,255), BOX7, 1)
        pygame.draw.rect(screen, (255,255,255), BOX8, 1)
        pygame.draw.rect(screen, (255,255,255), BOX9, 1)
        pygame.draw.rect(screen, (255,255,255), BOX10, 1)
        pygame.draw.rect(screen, (255,255,255), BOX11, 1)
        pygame.draw.rect(screen, (255,255,255), BOX12, 1)
        pygame.draw.rect(screen, (255,255,255), BOX13, 1)
        pygame.draw.rect(screen, (255,255,255), BOX14, 1)
        pygame.draw.rect(screen, (255,255,255), BOX15, 1)
        pygame.draw.rect(screen, (255,255,255), BOX16, 1)
        ##draw a rectangle for restart button
        pygame.draw.rect(screen, (255,255,255), (140,425, 150,50), 1)
        pygame.display.flip() ##udate the display

        #displays numbers on each box
        screen.blit(text1, (45, 30))
        screen.blit(text2, (148, 30))
        screen.blit(text3, (251, 30))
        screen.blit(text4, (354, 30))
        screen.blit(text5, (45, 133))
        screen.blit(text6, (148, 133))
        screen.blit(text7, (251, 133))
        screen.blit(text8, (354, 133))
        screen.blit(text9, (45, 236))
        screen.blit(text10, (138, 236))
        screen.blit(text11, (241, 236))
        screen.blit(text12, (344, 236))
        screen.blit(text13, (35, 339))
        screen.blit(text14, (138, 339))
        screen.blit(text15, (241, 339))
        screen.blit(text16, (344, 339))
        ##says "restart" on restart button
        screen.blit(text_restart, (180, 430))
        pygame.display.flip() ##updates the display

#simplifies all the rectangles into buttons
button1 = pygame.draw.rect(screen, (255,255,255), BOX1, 1)
button2 = pygame.draw.rect(screen, (255,255,255), BOX2, 1)
button3 = pygame.draw.rect(screen, (255,255,255), BOX3, 1)
button4 = pygame.draw.rect(screen, (255,255,255), BOX4, 1)
button5 = pygame.draw.rect(screen, (255,255,255), BOX5, 1)
button6 = pygame.draw.rect(screen, (255,255,255), BOX6, 1)
button7 = pygame.draw.rect(screen, (255,255,255), BOX7, 1)
button8 = pygame.draw.rect(screen, (255,255,255), BOX8, 1)
button9 = pygame.draw.rect(screen, (255,255,255), BOX9, 1)
button10 = pygame.draw.rect(screen, (255,255,255), BOX10, 1)
button11 = pygame.draw.rect(screen, (255,255,255), BOX11, 1)
button12 = pygame.draw.rect(screen, (255,255,255), BOX12, 1)
button13 = pygame.draw.rect(screen, (255,255,255), BOX13, 1)
button14 = pygame.draw.rect(screen, (255,255,255), BOX14, 1)
button15 = pygame.draw.rect(screen, (255,255,255), BOX15, 1)
button16 = pygame.draw.rect(screen, (255,255,255), BOX16, 1)
##restart button
button_restart = pygame.draw.rect(screen, (255,255,255), (140, 425, 150, 50), 1)

##while running, this loop will repeat
while running:
        grid() #displays the blank grid
        for e in pygame.event.get(): #for every event
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN: #if the event is a click
                pos = pygame.mouse.get_pos() ##the position is the position of the click
                if button_restart.collidepoint(pos): ##if the position of the click was in the restart button
                       ##reset all the variables
                        screen.fill((0,0,0))
                        turns = 40
                        round1 = round(0)
                        choice1 = 1
                        choice2 = 2
                        ##reshuffle the colors
                        random.shuffle(color_choices)
                        grid()
                        running = True
                elif button1.collidepoint(pos): ##if the click was in button1
                        pygame.draw.rect(screen, color_choices[0], BOX1) ##fill the box will the hidden color
                        turns -= 1 ##decrease turns for every click
                        if turns in even: #if it is an even turn, check for a match
                                box_choice2 = BOX1 ##keeps track of choice
                                choice2 = color_choices[0]
                                check_match()
                        else:
                                box_choice1 = BOX1  ##keeps track of choice
                                choice1 = color_choices[0]
                                choice2 = 0
                elif button2.collidepoint(pos): ##same thing for each button
                        pygame.draw.rect(screen, color_choices[1], BOX2)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX2
                                choice2 = color_choices[1]
                                check_match()
                
                        else:
                                box_choice1 = BOX2
                                choice1 = color_choices[1]
                                choice2 = 0
                elif button3.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[2], BOX3)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX3
                                choice2 = color_choices[2]
                                check_match()
                        else:
                                box_choice1 = BOX3
                                choice1 = color_choices[2]
                                choice2 = 0
                elif button4.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[3], BOX4)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX4
                                choice2 = color_choices[3]
                                check_match()
                        else:
                                box_choice1 = BOX4
                                choice1 = color_choices[3]
                                choice2 = 0
                        continue
                elif button5.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[4], BOX5)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX5
                                choice2 = color_choices[4]
                                check_match()
                        else:
                                box_choice1 = BOX5
                                choice1 = color_choices[4]
                                choice2 = 0                   
                elif button6.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[5], BOX6)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX6
                                choice2 = color_choices[5]
                                check_match()
                        else:
                                box_choice1 = BOX6
                                choice1 = color_choices[5]
                                choice2 = 0
                elif button7.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[6], BOX7)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX7
                                choice2 = color_choices[6]
                                check_match()
                        else:
                                box_choice1 = BOX7
                                choice1 = color_choices[6]
                                choice2 = 0
                elif button8.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[7], BOX8)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX8
                                choice2 = color_choices[7]
                                check_match()
                        else:
                                box_choice1 = BOX8
                                choice1 = color_choices[7]
                                choice2 = 0
                elif button9.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[8], BOX9)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX9
                                choice2 = color_choices[8]
                                check_match()
                        else:
                                box_choice1 = BOX9
                                choice1 = color_choices[8]
                                choice2 = 0
                elif button10.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[9], BOX10)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX10
                                choice2 = color_choices[9]
                                check_match()
                        else:
                                box_choice1 = BOX10
                                choice1 = color_choices[9]
                                choice2 = 0
                elif button11.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[10], BOX11)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX11
                                choice2 = color_choices[10]
                                check_match()
                        else:
                                box_choice1 = BOX11
                                choice1 = color_choices[10]
                                choice2 = 0
                elif button12.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[11], BOX12)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX12
                                choice2 = color_choices[11]
                                check_match()
                        else:
                                box_choice1 = BOX12
                                choice1 = color_choices[11]
                                choice2 = 0
                elif button13.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[12], BOX13)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX13
                                choice2 = color_choices[12]
                                check_match()
                        else:
                                box_choice1 = BOX13
                                choice1 = color_choices[12]
                                choice2 = 0
                elif button14.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[13], BOX14)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX14
                                choice2 = color_choices[13]
                                check_match()
                        else:
                                box_choice1 = BOX14
                                choice1 = color_choices[13]
                                choice2 = 0
                elif button15.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[14], BOX15)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX15
                                choice2 = color_choices[14]
                                check_match()
                        else:
                                box_choice1 = BOX15
                                choice1 = color_choices[14]
                                choice2 = 0
                elif button16.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[15], BOX16)
                        turns -= 1
                        if turns in even:
                                box_choice2 = BOX16
                                choice2 = color_choices[15]
                                check_match()
                        else:
                                box_choice1 = BOX16
                                choice1 = color_choices[15]
                                choice2 = 0
        pygame.display.flip() ##display screen