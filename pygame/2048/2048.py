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
        for square in squares:
            if square.value >= 1:
                for othersquare in squares:
                    if othersquare.value == 0 and othersquare.coords[0] == square.coords[0]:
                        for x in range(0,int(square.coords[1])):
                            if othersquare.value == 0:
                                othersquare.value += 1
                                square.value = 0            
                        break
    elif direction == 'left':
        for square in squares:
            if square.value >= 1:
                for othersquare in squares:
                    if othersquare.value == 0 and othersquare.coords[1] == square.coords[1]:
                        for x in range(0,int(square.coords[0])):
                            if othersquare.value == 0:
                                othersquare.value += 1
                                square.value = 0  
                        break                            

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

s1 = Square((0,0),0)
s2 = Square((1,0),0)
s3 = Square((2,0),0)
s4 = Square((3,0),0)

s5 = Square((0,1),0)
s6 = Square((1,1),0)
s7 = Square((2,1),0)
s8 = Square((3,1),0)

s9 = Square((0,2),0)
s10 = Square((1,2),0)
s11 = Square((2,2),0)
s12 = Square((3,2),0)

s13 = Square((0,3),0)
s14 = Square((1,3),0)
s15 = Square((2,3),0)
s16 = Square((3,3),0)              

squares = [s1,s2,s3,s4,
           s5,s6,s7,s8,
           s9,s10,s11,s12,
           s13,s14,s15,s16]

# col0 = [s1,s5,s9,s13] 
# col1 = [s2,s6,s10,s14]
# col2 = [s3,s7,s11,s15]
# col3 = [s4,s8,s12,s16]
# row0 = [s1,s2,s3,s4]
# row1 = [s5,s6,s7,s8]
# row2 = [s9,s10,s11,s12]
# row3 = [s13,s14,s15,s16]


valuetablerow0 = [s1.value,s2.value,s3.value,s4.value]
valuetablerow1 = [s5.value,s6.value,s7.value,s8.value]
valuetablerow2 = [s9.value,s10.value,s11.value,s12.value]
valuetablerow3 = [s13.value,s14.value,s15.value,s16.value]

valuetablecol0 = [s1.value,s5.value,s9.value,s13.value]
valuetablecol1= [s2.value,s6.value,s10.value,s14.value]
valuetablecol2 = [s3.value,s7.value,s11.value,s15.value]
valuetablecol3 = [s4.value,s8.value,s12.value,s16.value]

number_2 = pygame.image.load('squares/2.png').convert_alpha()
number_2_rect = number_2.get_rect(topleft = (65,65))
# number_4 = pygame.image.load('squares/4.png').convert_alpha()
# number_8 = pygame.image.load('squares/8.png').convert_alpha()
# number_16 = pygame.image.load('squares/16.png').convert_alpha()
# number_32 = pygame.image.load('squares/32.png').convert_alpha()

live_squares = []

debug = {pygame.K_5:s1,
         pygame.K_6:s2,
         pygame.K_7:s3,
         pygame.K_8:s4,
         pygame.K_t:s5,
         pygame.K_y:s6,
         pygame.K_u:s7,
         pygame.K_i:s8,
         pygame.K_g:s9,
         pygame.K_h:s10,
         pygame.K_j:s11,
         pygame.K_k:s12,
         pygame.K_b:s13,
         pygame.K_n:s14,
         pygame.K_m:s15,
         pygame.K_COMMA:s16}

screen.fill(bg_colour)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                for sq in squares:
                    sq.value = 0
            if event.key == pygame.K_SPACE:
                spawn()
            if event.key == pygame.K_UP:
                move('up')
            if event.key == pygame.K_DOWN:
                move('down')
            if event.key == pygame.K_LEFT:
                move('left')
            #DEBUG#    
            if event.key in debug:
                debug[event.key].value = 1
            #######
                
    for key in xy.keys():
        bg_square = pygame.draw.rect(screen,bg_square_colour,(xy[key][0],xy[key][1],160,160))
    for square in squares:
        if square.value == 1:
            screen.blit(number_2,xy[square.coords])
        
        

        
    
    pygame.display.update()
    clock.tick(60)