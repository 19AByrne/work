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
wh = pygame.display.get_desktop_sizes()[0]
print(wh)
height = wh[1]
width = wh[0]
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

scale = width/50
g = 9.8

initial = (3,4)

xshift = 0
yshift = 0

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

# print(xrange(initial))
print(maxheight(initial))

def parabola(init, xrange, maxheight):
    interval = 1000
    xpoints = []
    ypoints = []
    points = []
    for x in range(interval+1):
        xpoints.append(xrange/interval * x)
    for y in range(int(interval/2)+1):
        ypoints.append(maxheight/(interval) * 2*y)
    ypoints = ypoints[:int(interval/2)] + ypoints[int(interval/2)::-1]
#     print(len(xpoints))
#     print(len(ypoints))
    for i in range(len(xpoints)):
        points.append( (xpoints[i],ypoints[i]) )
    return points

def parabola(init, t):
    interval = 5


while running:
    for event in pygame.event.get():
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
                
            if event.key == pygame.K_SPACE:
                pass
                
    screen.fill("black")
    
    ground = pygame.Rect(0 , (height*7/8) - yshift ,width,height/8)
    pygame.draw.rect(screen, 'dark green', ground)
    
    pygame.draw.circle(screen, 'red', (width/8 -xshift,height*7/8 - yshift), 5) # origin
    pygame.draw.circle(screen, 'red', (width/8 + (xrange(initial)*scale) - xshift, height*7/8 - yshift), 5) #final pos
    maxpoint = (width/8 + (xrange(initial)*scale)/2 , (height*7/8) + (maxheight(initial)*scale)) #max height
#     print(maxpoint)

    pygame.draw.circle(screen, 'purple', (width/8 + (xrange(initial)*scale)/2 -xshift,  (height*7/8) - (maxheight(initial)*scale)-yshift), 5)
    
    for x in range(100):
        pygame.draw.circle(screen, 'blue', (width/8 + x*(scale)-xshift, (height*7/8) - yshift), 3)
    
    curvepoints = parabola(initial, xrange(initial), maxheight(initial))
    for p in curvepoints:
        pygame.draw.circle(screen, 'white', (width/8 + p[0]*scale -xshift, (height*7/8) - p[1]*scale - yshift), 3)

    pygame.display.flip()
    clock.tick(144)  # fps limit
