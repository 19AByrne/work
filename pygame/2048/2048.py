import pygame
from random import choice
from sys import exit

class Square:
    def __init__(self,coords,value):
        self.value = value
        self.coords = coords

def spawn():
    spawnpoint = choice(squares)
    while spawnpoint.value != 0:
        spawnpoint = choice(squares)
    spawnpoint.value += 1
    
def move(direction):
    if direction == 'up':
        
#         for x in range(4):
#             above_squares = [square
        for square in squares:                                           
            for othersquare in squares:
                if othersquare.coords[1] == square.coords[1]:
                    if othersquare.coords[0] == 0:
                        if othersquare.value == 0:
                            pass
                            #decrease sq=uare value and increase this square value
                    
    
pygame.init()
scwidth = 800
scheight = 800
running = True
game_active = True
screen = pygame.display.set_mode((scwidth,scheight))
pygame.display.set_caption('2048')
clock = pygame.time.Clock()

bg_colour = (191, 191, 191)

bg_square_colour = (145, 145, 145)


xy = {(0,0):(65,65),
              (1,0):(235,65),
              (2,0):(405,65),
              (3,0):(575,65),
              
              (0,1):(65,235),
              (1,1):(235,235),
              (2,1):(405,235),
              (3,1):(575,235),
              
              (0,2):(65,405),
              (1,2):(235,405),
              (2,2):(405,405),
              (3,2):(575,405),
              
              (0,3):(65,575),
              (1,3):(235,575),
              (2,3):(405,575),
              (3,3):(575,575),}

s1 = Square(xy[0,0],0)
s2 = Square(xy[1,0],0)
s3 = Square(xy[2,0],0)
s4 = Square(xy[3,0],0)

s5 = Square(xy[0,1],0)
s6 = Square(xy[1,1],0)
s7 = Square(xy[2,1],0)
s8 = Square(xy[3,1],0)

s9 = Square(xy[0,2],0)
s10 = Square(xy[1,2],0)
s11 = Square(xy[2,2],0)
s12 = Square(xy[3,2],0)

s13 = Square(xy[0,3],0)
s14 = Square(xy[1,3],0)
s15 = Square(xy[2,3],0)
s16 = Square(xy[3,3],0)              

squares = [s1,s2,s3,s4,
           s5,s6,s7,s8,
           s9,s10,s11,s12,
           s13,s14,s15,s16]

number_2 = pygame.image.load('squares/2.png').convert_alpha()
number_2_rect = number_2.get_rect(topleft = (65,65))
number_4 = pygame.image.load('squares/4.png').convert_alpha()
number_8 = pygame.image.load('squares/8.png').convert_alpha()
number_16 = pygame.image.load('squares/16.png').convert_alpha()
number_32 = pygame.image.load('squares/32.png').convert_alpha()

live_squares = []

screen.fill(bg_colour)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spawn()
            if event.key == pygame.K_UP:
                move('up')
    for key in xy.keys():
        bg_square = pygame.draw.rect(screen,bg_square_colour,(xy[key][0],xy[key][1],160,160))
    for square in squares:
        if square.value == 1:
            screen.blit(number_2,square.coords)
        
        

        
    
    pygame.display.update()
    clock.tick(60)
