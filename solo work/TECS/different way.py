import pygame
import math
# import sympy




'''main use''' 
# pygame.init()
# wh = pygame.display.get_desktop_sizes()[0]
# height = wh[1]
# width = wh[0]
# screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
# clock = pygame.time.Clock()
# running = True

'''debugging mode'''
pygame.init()
height = 1026
width = 1824
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, depth=0, display=1)
clock = pygame.time.Clock()
running = True



scale = width/50
g = 9.8

initial = (10,10)

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
# print(maxheight(initial))

# print(time(initial))

# def parabola(init, t):
#     interval = 9999
#     times = [(t*x)/interval for x in range(interval+1)]
#     ypoints = [(initial[1]*time) - ((g/2)*(time**2)) for time in times]
#     xpoints = [(initial[0]*time) for time in times]
#     points = [ (xpoints[i],ypoints[i]) for i in range(len(xpoints)) ]
#     return points

def fire(init, t):
    print(t)
    time = round(t*1000) #need to round because timer cannot contain float
    pygame.time.set_timer(landing, time, 1) #not sure what the first parameter means , 1 = loop parameter
    times = [(t*x)/time for x in range(time)]
    #if i dont use (time+1) the lengths of intervals and ms wll be equal but the final position(landing coord) will not be included, not sure if creates issues
    for time in times:
        pygame.draw.circle(screen, 'white', (width/8 + (init[0]*time)*scale -xshift, (height*7/8) - ((init[1]*time) - ((g/2)*(time**2)))*scale - yshift), 1)

def calculate_pos(t, ux, uy, g, scale):
    x = (width/8 +(ux*t)*scale - xshift)
    y = (height*7/8 - (uy*t - (g/2)*(t**2))*scale - yshift)
    return (x,y)
    
landing = pygame.event.custom_type()
per_ms = pygame.event.custom_type()

curvepoints = []
while running:
    dT = clock.get_time()
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
                pygame.time.set_timer(landing, round(time(initial)*1000), 1)
                
                airtime = time(initial)
                current_time = pygame.time.get_ticks() / 1000
                if current_time < airtime:
                    pos = calculate_pos(current_time, initial[0], initial[1], g, scale)
                    curvepoints.append(pos)
            
        
        if event.type == landing:
            print(f'{time(initial)} elapsed')
            
                
    screen.fill("black")
    
    ground = pygame.Rect(0 , (height*7/8) - yshift ,width,height/8)
    pygame.draw.rect(screen, 'dark green', ground) #ground
    
    pygame.draw.circle(screen, 'red', (width/8 -xshift,height*7/8 - yshift), 5) # origin
    pygame.draw.circle(screen, 'red', (width/8 + (xrange(initial)*scale) - xshift, height*7/8 - yshift), 5) #final pos
    maxpoint = (width/8 + (xrange(initial)*scale)/2 , (height*7/8) + (maxheight(initial)*scale)) #max height


    pygame.draw.circle(screen, 'purple', (width/8 + (xrange(initial)*scale)/2 -xshift,  (height*7/8) - (maxheight(initial)*scale)-yshift), 5)
    
    for x in range(100):
        pygame.draw.circle(screen, 'blue', (width/8 + x*(scale)-xshift, (height*7/8) - yshift), 3)
        
    for point in curvepoints:
        pygame.draw.circle(screen, 'white', point, 3)

    pygame.display.flip()
    clock.tick(60)  # fps limit
