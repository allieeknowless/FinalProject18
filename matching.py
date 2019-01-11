import pygame
import time
import random
from random import shuffle

pygame.init()
screen = pygame.display.set_mode((418, 418))
done = False

my_font = pygame.font.SysFont("Arial", 48)
my_font2 = pygame.font.SysFont("Arial", 28)

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
color13 = (210, 0, 255)
color14 = (190, 0, 255)
color15 = (190,200,200)
color16 = (200,200,200)
color_choices = [(color1), (color2), (color3), (color4), (color5), (color6), (color7), (color8), (color9), (color10), (color11), (color12), (color13), (color14), (color15), (color16)]

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
    while not done:
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

        time.sleep(4)
        pygame.quit()

def grid_hidden():
    '''flips the card when a user chooses it'''
    random.shuffle(color_choices)
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