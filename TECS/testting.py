# Example file showing a basic pygame "game loop"
import pygame
# import math
# import sympy

'''debugging mode'''
pygame.init()
height = 1026
width = 1824
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, depth=0, display=1)
clock = pygame.time.Clock()
running = True

'''commercial use''' #pygame.display.get_desktop_sizes <<<<use that like
# pygame.init()
# height = 1080
# width = 1920
# screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
# clock = pygame.time.Clock()
# running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
#                 running = False
    screen.fill("black")
    
    ground = pygame.Rect(0,height*7/8,width,height/8)
    pygame.draw.rect(screen, 'dark green', ground)
    
    pygame.draw.circle(screen, 'red', (width/8,height*7/8), 5)
    
    pygame.display.flip()
    clock.tick(144)  # fps limit