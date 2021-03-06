import pygame 
import time
import random
from random import shuffle

x = 0
y = 0

pygame.init()
<<<<<<< HEAD
screen = pygame.display.set_mode((418, 418))
running = True
=======
screen = pygame.display.set_mode((418, 418)) #sets screen size
done = False ##used for loop

my_font = pygame.font.SysFont("Arial", 48) 
my_font2 = pygame.font.SysFont("Arial", 28)

#List of colors to be used for matching. 2 of each color to make pairs
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
random.shuffle(color_choices)

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



def welcome_screen():
    ''' screen to welcome users'''
    pygame.draw.rect(screen, (255,255,255), (115, 175, 150, 50),1)
    pygame.draw.rect(screen, (255,255,255), (115, 240, 150, 50),1)
    pygame.display.flip()
    matching_text = my_font.render("Matching Game!", True, (125, 255, 255))
    instructions_text = my_font2.render("Instructions", True, (255, 255, 255))
    start_text = my_font2.render("Start", True, (255, 255, 255))
    screen.blit(matching_text, (70, 100))
    screen.blit(instructions_text, (131, 180))
    screen.blit(start_text, (161, 250))
    pygame.display.flip()

    time.sleep(4)
    pygame.quit()

def instructions():
    '''instructions for the game'''
    instructions_screen = my_font2.render("insert instructions", True, (255, 255, 255))
    screen.blit(instructions_screen, (10, 10))
    pygame.display.flip()

    time.sleep(4)
    pygame.quit()

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
        pygame.display.flip() 

<<<<<<< HEAD
 

while running:
     grid()
     for e in pygame.event.get():
           if e.type == pygame.QUIT:
               running = False
           if e.type == pygame.MOUSEBUTTONDOWN:
               pos = pygame.mouse.get_pos()
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
               if button1.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[0], BOX1)
               if button2.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[1], BOX2)
               if button3.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[2], BOX3)
               if button4.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[3], BOX4)
               if button5.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[4], BOX5)
               if button6.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[5], BOX6)
               if button7.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[6], BOX7)
               if button8.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[7], BOX8)
               if button9.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[8], BOX9)
               if button10.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[9], BOX10)
               if button11.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[10], BOX11)
               if button12.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[11], BOX12)
               if button13.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[12], BOX13)
               if button14.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[13], BOX14)
               if button15.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[14], BOX15)
               if button16.collidepoint(pos):
                    pygame.draw.rect(screen, color_choices[15], BOX16)

     pygame.display.flip()
=======
        time.sleep(4)
        pygame.quit()

def grid_hidden():
    '''flips the card when a user chooses it'''
    random.shuffle(color_choices) ##each square gets a different color every time
    pygame.draw.rect(screen, color_choices[0], BOX1)
    pygame.draw.rect(screen, color_choices[1], BOX2)
    pygame.draw.rect(screen, color_choices[2], BOX3)
    pygame.draw.rect(screen, color_choices[3], BOX4)
    pygame.draw.rect(screen, color_choices[4], BOX5)
    pygame.draw.rect(screen, color_choices[5], BOX6)
    pygame.draw.rect(screen, color_choices[6], BOX7)
    pygame.draw.rect(screen, color_choices[7], BOX8)
    pygame.draw.rect(screen, color_choices[8], BOX9)
    pygame.draw.rect(screen, color_choices[9], BOX10)
    pygame.draw.rect(screen, color_choices[10], BOX11)
    pygame.draw.rect(screen, color_choices[11], BOX12)
    pygame.draw.rect(screen, color_choices[12], BOX13)
    pygame.draw.rect(screen, color_choices[13], BOX14)
    pygame.draw.rect(screen, color_choices[14], BOX15)
    pygame.draw.rect(screen, color_choices[15], BOX16)
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
    pygame.display.flip() 

    time.sleep(4)
    pygame.quit()

grid_hidden()
>>>>>>> 02610986a1e39b32a68454117ff773cd15f9125b
