import pygame
from sys import exit
pygame.init()
sw = (400)
sh = (400)
screen = pygame.display.set_mode((sw,sh))
clock = pygame.time.Clock()
bird = pygame.image.load('graphics/bird.png').convert_alpha()
bird_rect = bird.get_rect(center = (200,200))
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255,255,255))
    screen.blit(bird,bird_rect)
    pygame.display.update()