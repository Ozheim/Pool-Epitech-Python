from pygame import *
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

fond = pygame.image.load('hangman/asset/pendaison.jpg')
screen.blit(fond,(0,0))

while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


   
    pygame.display.flip()

    clock.tick(60)  
    pygame.draw.circle(screen, "white", (300,100), 50)
    
    pygame.draw.line(screen, "white",(300,100), (300,400),width=5 )
    pygame.draw.line(screen, "white",(200,300), (300,200),width=5 )
    pygame.draw.line(screen, "white",(300,200), (400,300),width=5 )
    pygame.draw.line(screen, "white",(200,500), (300,400),width=5 )
    pygame.draw.line(screen, "white",(300,400), (400,500),width=5 )


pygame.quit()



