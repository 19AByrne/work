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

initial = (1,1)

xshift = 0
yshift = 0

fontsize = 50
font = pygame.font.Font('Font/sylfaen.ttf', fontsize)

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

InputterStates = [pygame.image.load('Images/IJ.png').convert_alpha(),
                    pygame.image.load('Images/IJselectedI.png').convert_alpha(),
                    pygame.image.load('Images/IJselectedJ.png').convert_alpha()]
Inputter = InputterStates[0]
Inputter_rect = Inputter.get_rect(center=(width/12,height/7))
I_rect = pygame.Rect(Inputter_rect.left+12,Inputter_rect.top+25, 50, 50)
J_rect = pygame.Rect(Inputter_rect.left+120,Inputter_rect.top+25, 50, 50)
Ivalue = font.render(str(initial[0]), False, (64,64,64))
Jvalue = font.render(str(initial[1]), False, (64,64,64))
Ivalue_rect = pygame.Rect(I_rect.left,I_rect.top,fontsize,fontsize)
Jvalue_rect = pygame.Rect(J_rect.left+(fontsize/2),J_rect.top+(fontsize/2),fontsize,fontsize)
Ivalue_rect.center = I_rect.center 

landing = pygame.event.custom_type()
per_ms = pygame.event.custom_type()
simulating = False
landed = False
originstate = True
curvepoints = []
totalT = 0
inputting = False
showmax = False
showfinal = False

while running:
    dT = clock.get_time()
    theta = math.degrees(math.atan(initial[1]/initial[0]))
    mag = math.sqrt((initial[0])**2+(initial[1])**2)
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
            
            if I_rect.collidepoint(event.pos):
                if originstate:
                    Inputter = InputterStates[1]
                    inputting = True
                    selected = 'i'
                    emptyvalue = ''
            if J_rect.collidepoint(event.pos):
                if originstate:
                    Inputter = InputterStates[2]
                    inputting = True
                    selected = 'j'
                    emptyvalue = ''                
                
        if event.type == pygame.KEYDOWN:
            if inputting and originstate:
                if event.key >= 48 and event.key <= 57:
                    emptyvalue = emptyvalue + str(pygame.key.name(event.key))
                if event.key == pygame.K_PERIOD:
                    emptyvalue = emptyvalue + str(pygame.key.name(event.key))
                if event.key == pygame.K_RETURN:
                    if selected == 'i':
                        initial = ( float(emptyvalue), initial[1] )
                    if selected == 'j':
                        initial = ( initial[0], float(emptyvalue) )
#                 print(event.key,pygame.key.name(event.key))
            
            
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




        if event.type == landing:
            simulating = False
            landed = True
            print(f'{time(initial)} elapsed') #not necessary
            
    screen.fill("black")
    
    ground = pygame.Rect(0 , (height*7/8) - yshift ,width,height/8)
    pygame.draw.rect(screen, 'dark green', ground) #ground
    
    for x in range(100):
        pygame.draw.circle(screen, 'blue', (width/8 + x*(scale)-xshift, (height*7/8) - yshift), 3)
        
    if simulating:
        mousepos = pygame.mouse.get_pos()
        if FireButton_rect.collidepoint(mousepos):
            FireButton = FireButtonStates[2]
        else:
            FireButton = FireButtonStates[1]
        totalT += dT
#         print(totalT/1000)
        pos = calculate_pos(totalT/1000, initial[0], initial[1], g, scale)
        path.append(pos)


    if originstate:
        FireButton = FireButtonStates[0]
    else:
        if showtrail:
            for p in path:
                pygame.draw.circle(screen, 'white', ( (width/8 + p[0]*scale - xshift),  (height*7/8 - p[1]*scale - yshift))  , 3)
            if totalT > (time(initial)*1000)/2:
                showmax = True
                pygame.draw.circle(screen, 'red', (width/8 + ((( (mag**2) * (math.sin(2*math.radians(theta))) ) / g)*scale)/2 -xshift,  (height*7/8) - ((( (mag**2) * (math.sin(math.radians(theta)))*(math.sin(math.radians(theta))) ) / (2*g))*scale)-yshift), 5)
            if totalT >= (time(initial)*1000):
                simulating = False
                pygame.draw.circle(screen, 'red', (width/8 + ((( (mag**2) * (math.sin(2*math.radians(theta))) ) / g)*scale) - xshift, height*7/8 - yshift), 5)
        else:
            pygame.draw.circle(screen, 'white', ( (width/8 + pos[0]*scale - xshift),  (height*7/8 - pos[1]*scale - yshift)), 3)
            
    pygame.draw.circle(screen, 'red', (width/8 -xshift,height*7/8 - yshift), 5) # origin
#     pygame.draw.circle(screen, 'red', (width/8 + ((( (mag**2) * (math.sin(2*math.radians(theta))) ) / g)*scale) - xshift, height*7/8 - yshift), 5) #final pos
# maxpoint = (width/8 + (xrange(initial)*scale)/2 , (height*7/8) + (maxheight(initial)*scale))

    
    screen.blit(FireButton,FireButton_rect)
    screen.blit(ResetButton, ResetButton_rect)
    screen.blit(ShowTrailButton, ShowTrailButton_rect)
    screen.blit(Inputter,Inputter_rect)
    screen.blit(Ivalue, Ivalue_rect)
    screen.blit(Jvalue, Jvalue_rect)
    pygame.display.flip()
    clock.tick(144)  # fps limit


