import pygame
import time
pygame.init()
my_font = pygame.font.SysFont("Arial", 48)
screen = pygame.display.set_mode((418, 418))
done = False

#BOX1 = pygame.draw.rect(screen, (255,255,255), [5, 5, 100, 100], 1)
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
    

