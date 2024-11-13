import pygame
import math
# import sympy




'''main use''' 
pygame.init()
wh = pygame.display.get_desktop_sizes()[0]
height = wh[1]
width = wh[0]
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

'''debugging mode'''
# pygame.init()
# height = 1026
# width = 1824
# screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, depth=0, display=1)
# clock = pygame.time.Clock()
# running = True

scale = width/50
g = 9.8

initial = (3,4)

xshift = 0
yshift = 0

theta = math.degrees(math.atan(initial[1]/initial[0]))
mag = math.sqrt((initial[0])**2+(initial[1])**2)

def time(init):
    return ((init[1])) / (4.9)

# def xrange2(init):                  not using this function because it relies on another function
#     return (init[0]) * (time(init))

def xrange(init):
    return ( (mag**2) * (math.sin(2*math.radians(theta))) ) / g

def maxheight(init):
    return ( (mag**2) * (math.sin(math.radians(theta)))*(math.sin(math.radians(theta))) ) / (2*g)

def calculate_pos(t, ux, uy, g, scale):
    x = (ux*t)
    y = (uy*t - (g/2)*(t**2))
    return (x,y)

    
FireButtonStates = [pygame.image.load('Images/Fire!.png').convert_alpha(),
                    pygame.image.load('Images/Fire! italic.png').convert_alpha(),
                    pygame.image.load('Images/Fire! strike.png').convert_alpha()]
FireButton = FireButtonStates[0]
FireButton_rect = FireButton.get_rect(center=(width/12,height/4))

ResetButton = pygame.image.load('Images/reset.png').convert_alpha()
ResetButton_rect = ResetButton.get_rect(center=(width/12, height/3))

ShowTrailButton_States = [pygame.image.load('Images/ShowTrail.png').convert_alpha(),
                          pygame.image.load('Images/XShowTrail.png').convert_alpha()]
showtrail = False
ShowTrailButton = ShowTrailButton_States[showtrail]
ShowTrailButton_rect = ShowTrailButton.get_rect(center=(width/12,height*7.69/19))

landing = pygame.event.custom_type()
per_ms = pygame.event.custom_type()
simulating = False
landed = False
originstate = True
curvepoints = []
totalT = 0

while running:
    dT = clock.get_time()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if FireButton_rect.collidepoint(event.pos):
                if not simulating and originstate:
                    pygame.time.set_timer(landing, round(time(initial)*1000), 1)
                    simulating = True
                    originstate = False
                    path = []
            if ResetButton_rect.collidepoint(event.pos):
                simulating = False
                landed = False
                originstate = True
                curvepoints = []
                totalT = 0
                path = []
            if ShowTrailButton_rect.collidepoint(event.pos):
                showtrail = not showtrail
                ShowTrailButton = ShowTrailButton_States[showtrail]
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
            if event.key == pygame.K_UP:
                yshift -= 10
            if event.key == pygame.K_DOWN:
                if yshift != 0:
                    yshift += 10
            if event.key == pygame.K_RIGHT:
                xshift += 10
            if event.key == pygame.K_LEFT:
                if xshift != 0:
                    xshift -=10
            
            if event.key == pygame.K_i:
                scale += 1
            if event.key == pygame.K_o:
                scale -= 1
                
            if event.key == pygame.K_r:
                xshift, yshift = 0,0
                scale = width/50
                
            ####keys to be turned into buttons                
            if event.key == pygame.K_n:
                showtrail = not showtrail
             
        if event.type == landing:
            simulating = False
            landed = True
            print(f'{time(initial)} elapsed') #not necessary
            
    screen.fill("black")
    
    if simulating or not originstate:
        mousepos = pygame.mouse.get_pos()
        if FireButton_rect.collidepoint(mousepos):
            FireButton = FireButtonStates[2]
        else:
            FireButton = FireButtonStates[1]
        totalT += dT
#         print(totalT/1000)
        pos = calculate_pos(totalT/1000, initial[0], initial[1], g, scale)
        path.append(pos)
        if showtrail:
            for p in path:
                pygame.draw.circle(screen, 'white', ( (width/8 + p[0]*scale - xshift),  (height*7/8 - p[1]*scale - yshift))  , 3)
            if totalT > (time(initial)*1000)/2:
                pygame.draw.circle(screen, 'purple', (width/8 + (xrange(initial)*scale)/2 -xshift,  (height*7/8) - (maxheight(initial)*scale)-yshift), 5)
        else:
            pygame.draw.circle(screen, 'white', ( (width/8 + pos[0]*scale - xshift),  (height*7/8 - pos[1]*scale - yshift)), 3)

    if originstate:
        FireButton = FireButtonStates[0]
    ground = pygame.Rect(0 , (height*7/8) - yshift ,width,height/8)
    pygame.draw.rect(screen, 'dark green', ground) #ground
    
    pygame.draw.circle(screen, 'red', (width/8 -xshift,height*7/8 - yshift), 5) # origin
    pygame.draw.circle(screen, 'red', (width/8 + (xrange(initial)*scale) - xshift, height*7/8 - yshift), 5) #final pos
# maxpoint = (width/8 + (xrange(initial)*scale)/2 , (height*7/8) + (maxheight(initial)*scale))

    for x in range(100):
        pygame.draw.circle(screen, 'blue', (width/8 + x*(scale)-xshift, (height*7/8) - yshift), 3)
    
    screen.blit(FireButton,FireButton_rect)
    screen.blit(ResetButton, ResetButton_rect)
    screen.blit(ShowTrailButton, ShowTrailButton_rect)
    pygame.display.flip()
    clock.tick(60)  # fps limit


