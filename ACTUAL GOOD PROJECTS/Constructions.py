# Example file showing a basic pygame "game loop"
import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

def slope(p1,p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])



radius = 7.5

points = []
positions = []

HOVER = False
HELD = False
showtri = False
showincircle = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #1 = lmb#
                if len(positions) == 3:
                    pass
                else:
                    positions.append(pygame.mouse.get_pos())
                    points.append(pygame.draw.circle)
        if event.type == pygame.MOUSEBUTTONDOWN and HOVER == True:
            if event.button == 3: #3 = rmb
                HELD = True
        if event.type == pygame.MOUSEBUTTONUP and HELD == True:
            if event.button == 3:
                HELD = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                points = []
                positions = []
            if event.key == pygame.K_t:
                showtri = not showtri
            if event.key == pygame.K_i:
                showincircle = not showincircle
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
   
    if len(positions) > 0:
        distances = [distance(pygame.mouse.get_pos(),x) for x in positions]
        closest = min(distances)
        closesti = distances.index(closest)
        if distance(pygame.mouse.get_pos(),positions[closesti]) < radius:
            hoveringi = closesti
            HOVER = True
        else:
            HOVER = False
            
    if HELD:
        positions[hoveringi] = pygame.mouse.get_pos()
    
    if len(points) == 3 and showtri == True:
        lines = [pygame.draw.line(screen, 'white', positions[0], positions[1], 4),
                 pygame.draw.line(screen, 'white', positions[1], positions[2], 4),
                 pygame.draw.line(screen, 'white', positions[2], positions[0], 4)]
        
    if len(points) == 3 and showincircle:
        lengths = [(distance(positions[0],positions[1])),
                   (distance(positions[1],positions[2])),
                   (distance(positions[2],positions[0]))] 
        T = abs(math.atan(((slope(positions[0],positions[1]))-(slope(positions[1],positions[2])))/(1+(slope(positions[0],positions[1])*(slope(positions[1],positions[2]))))))
        Area = (1/2)*lengths[0]*lengths[1]*math.sin(T)
        incentre = [(lengths[0]*positions[2][0]+lengths[1]*positions[0][0]+lengths[2]*positions[1][0])/sum(lengths),
                    (lengths[0]*positions[2][1]+lengths[1]*positions[0][1]+lengths[2]*positions[1][1])/sum(lengths)]
#         pygame.draw.circle(screen,'pink', incentre, radius)
        inradius = (2*Area)/sum(lengths)
        pygame.draw.circle(screen, 'pink',incentre,inradius,3)
        
    for i,p in enumerate(points):
        if i == hoveringi:
            p(screen, 'green', positions[i], radius)
        else:
            p(screen, 'white', positions[i], radius)
            
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()