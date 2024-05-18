# Example file showing a basic pygame "game loop"
import pygame
import math

# pygame setup
pygame.init()
height = 720
width = 1280
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

length = 10

squares = [] 
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #1 = lmb#
                squares.append()
                print('sqaure')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('space')
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    
    screen.fill("black")
    for square in squares:
        
        pygame.draw.rect(screen, 'white', square)
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()