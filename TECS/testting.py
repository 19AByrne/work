# Example file showing a basic pygame "game loop"
import pygame
import math
# import sympy

'''debugging mode'''
# pygame.init()
# height = 1026
# width = 1824
# screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, depth=0, display=1)
# clock = pygame.time.Clock()
# running = True

'''commercial use''' #pygame.display.get_desktop_sizes <<<<use that like
pygame.init()
height = 1080
width = 1920
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

scale = width/50
g = 9.8

initial = (6,24)


theta = math.degrees(math.atan(initial[1]/initial[0]))
mag = math.sqrt((initial[0])**2+(initial[1])**2)

def time(init):
    return (-(init[1])) / (-4.9)

# def xrange2(init):                  not using this function because it relies on another function
#     return (init[0]) * (time(init))

def xrange(init):
    return ( (mag**2) * (math.sin(2*math.radians(theta))) ) / g

def maxheight(init):
    return ( (mag**2) * (math.sin(math.radians(theta)))*(math.sin(math.radians(theta))) ) / (2*g)

print(xrange(initial))
print(maxheight(initial))


while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
    screen.fill("black")
    
    ground = pygame.Rect(0,height*7/8,width,height/8)
    pygame.draw.rect(screen, 'dark green', ground)
    
    pygame.draw.circle(screen, 'red', (width/8,height*7/8), 5)
    pygame.draw.circle(screen, 'red', (width/8 + (xrange(initial)*scale), height*7/8), 5)
    maxpoint = (width/8 + (xrange(initial)*scale)/2 , (height*7/8) + (maxheight(initial)*scale))
    print(maxpoint)

    pygame.draw.circle(screen, 'purple', (width/8 + (xrange(initial)*scale)/2 , (height*7/8) - (maxheight(initial)*scale)), 5)
    
    for x in range(43):
        pygame.draw.circle(screen, 'blue', (width/8 + x*(scale), height*7/8), 3)
    pygame.display.flip()
    clock.tick(144)  # fps limit