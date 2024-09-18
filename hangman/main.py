import pygame


pygame.init()

from pygame.locals import *

while True: 
    fenetre = pygame.display.set_mode((600, 600))
    
    if pygame.mouse.get_pressed(): 
        pygame.quit()
        
