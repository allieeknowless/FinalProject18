import pygame ##import pygame module
import time ##imports time module
import random  ##imports random module
from random import shuffle ##Used to randomly shuffle the board each round

update1 = 0 
update2 = 0

choice1 = 1
choice2 = 2

pygame.init() #initializes pygame's submodules
screen = pygame.display.set_mode((418, 490)) ##sets the screen size
running = True ## to control while loop

turns = 0 ##keeps track of how many turns the player has taken
matches = 0 ##keeps track of how many matches the player made

my_font = pygame.font.SysFont("Arial", 48) #set the font for the title
my_font2 = pygame.font.SysFont("Arial", 28) #sets font for the grid labels


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
color_choices = [(color1), (color2), (color3), (color4), (color5), (color6), (color7), (color8), (color9), (color10), (color11), (color12), (color13), (color14), (color15), (color16)]
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

#labels for all 16 boxes
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
text_instructions = my_font2.render("instructions", True, (255, 255, 255))

##keeps track of when it is an even round 
even = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80]

def update():
        pygame.display.flip()
        grid()
        pygame.time.wait(500)
        pygame.draw.rect(screen, (0,0,0), box_choice1)
        pygame.draw.rect(screen, (0,0,0), box_choice2)
        

def check_match():
        '''checks to see if a match has been made'''
        #time.sleep(5)
        if box_choice1 == box_choice2:
                print ("stop please")
                update()
        elif choice1 == choice2: ##if the two colors match
                global matches
                matches += 1
                if matches == 8:
                        print ("WINNNER")
                else:
                        print("match") ##keep the colors there and print 'match'
        else:##if the two colors do not match
                        print("no") ## print 'no'
                        update()

def grid():
        '''creates a numbered grid of 16 rectangles''' 
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
        pygame.draw.rect(screen, (255,255,255), (30,425, 150,50), 1)

        pygame.display.flip() 

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
        screen.blit(text_instructions, (50, 430))
        pygame.display.flip() 

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
#button_instructions = pygame.draw.rect()


while running:
        grid()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button1.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[0], BOX1)
                        turns +=1
                        if turns in even:
                                box_choice2 = BOX1
                                choice2 = color_choices[0]
                                check_match()
                        else:
                                box_choice1 = BOX1
                                choice1 = color_choices[0]
                                choice2 = 0
                elif button2.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[1], BOX2)
                        turns +=1
                        if turns in even:
                                box_choice2 = BOX2
                                choice2 = color_choices[1]
                                check_match()
                                #pygame.draw.rect(screen, (0,0,0), box_choice1)
                                #pygame.draw.rect(screen, (0,0,0), box_choice2)
                        else:
                                box_choice1 = BOX2
                                choice1 = color_choices[1]
                                choice2 = 0
                        #continue
                elif button3.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[2], BOX3)
                        turns +=1
                        if turns in even:
                                box_choice2 = BOX3
                                choice2 = color_choices[2]
                                check_match()
                                #pygame.draw.rect(screen, (0,0,0), box_choice1)
                                #pygame.draw.rect(screen, (0,0,0), box_choice2)
                        else:
                                box_choice1 = BOX3
                                choice1 = color_choices[2]
                                choice2 = 0
                        #continue
                elif button4.collidepoint(pos):
                        pygame.draw.rect(screen, color_choices[3], BOX4)
                        turns +=1
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
                        turns +=1
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
                        turns +=1
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
                        turns +=1
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
                        turns +=1
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
                        turns +=1
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
                        turns +=1
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
                        turns +=1
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
                        turns +=1
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
                        turns += 1
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
                        turns +=1
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
                        turns +=1
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
                        turns +=1
                        if turns in even:
                                box_choice2 = BOX16
                                choice2 = color_choices[15]
                                check_match()
                        else:
                                box_choice1 = BOX16
                                choice1 = color_choices[15]
                                choice2 = 0
        pygame.display.flip()
