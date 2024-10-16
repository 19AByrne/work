"""
   _____ ____  _   _ _______ _____   ____  _       _____ 
  / ____/ __ \| \ | |__   __|  __ \ / __ \| |     / ____|
 | |   | |  | |  \| |  | |  | |__) | |  | | |    | (___  
 | |   | |  | | . ` |  | |  |  _  /| |  | | |     \___ \ 
 | |___| |__| | |\  |  | |  | | \ \| |__| | |____ ____) |
  \_____\____/|_| \_|  |_|  |_|  \_\\____/|______|_____/ 

1 - switch to triangle mode
2 - switch to circle mode

Left mouse button - place point (dependent on mode)
right mouse button - drag any points (hold)

q - lock/unlock radius of circle
w - place outside tangent point
s - show tangent from that point

t - show triangle (when 3 points)
i - show incircle (when 3 points)
c - show circumcircle (when 3 points)

r - reset

"""
# Example file showing a basic pygame "game loop"
import pygame
import math
import sympy

# pygame setup
pygame.init()
height = 720
width = 1280
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

class Line:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
        self.yint = -c/y
        try:
            self.m = (-x/y)
            self.m2 = -(1/self.m)
        except ZeroDivisionError:
            self.m = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            self.m2 = 0
            
class LineSegment:
    def __init__(self,p1,p2,show):
        self.p1 = p1
        self.p2 = p2
        self.length = distance(p1,p2)
        self.M = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
        try:
            self.m = (p2[1]-p1[1])/(p2[0]-p1[0])
            self.m2 = -1/((p2[1]-p1[1])/(p2[0]-p1[0]))
        except ZeroDivisionError:
            self.m = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            self.m2 = 0
        if show:
            pygame.draw.line(screen,'white',p1,p2,4)
        
class Circle:
    def __init__(self,h,k,r):
        self.h = h
        self.k = k
        self.r = math.sqrt(r)
        self.centre = (h,k)
        
def distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

def slope(p1,p2):
    if p2[0] == p1[0]:
        return 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    else:
        return (p2[1]-p1[1])/(p2[0]-p1[0])
    
def perpslope(p1,p2):
    if p2[0] == p1[0]: return 1
    else: return -1/slope(p1,p2)

def Mid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def linegeneral(p,m):
    return Line(m,-1,-(m*p[0]+p[1]))

def simultaneous(l1,l2):
    if l1.x == 0:
        l1.x = 0.00000000000000000000000000000000000001
    if l2.x == 0:
        l2.x = 0.00000000000000000000000000000000000001
    coef1 = [l1.x,l1.y,l1.c]
    coef2 = [l2.x,l2.y,l2.c]
    
    p = -coef1[0]/coef2[0]
    newcoef = [c*p for c in coef2]
    b = coef1[1]+newcoef[1]
    c = -(coef1[2]+newcoef[2])
    y = c/b
    x = (y*coef1[1]+coef1[2])/-(coef1[0])
    return (x,y)

radius = 7.5

points = []
positions = []

tripoints = []
tripositions = []

circlepoints = []
circlepositions = []
circumpoints = []
circumpositions = []


HOVER = False
HELD = False
showtri = False
showincircle = False
showcircum = False
MODE = 1
centre = False
circum = False
lockradius = False
showtan = False

circleindex = 'N/A'
circumindex = 'N/A'
outpos = 'N/A'
outposindex = 'N/A'


while running:
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN and HOVER == True:
                if event.button == 3: #3 = rmb
                    HELD = True
        if event.type == pygame.MOUSEBUTTONUP and HELD == True:
                if event.button == 3:
                    HELD = False
                    
                    
        if MODE == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #1 = lmb#
                    if len(tripositions) == 3:
                        pass
                    else:
                        tripositions.append(pygame.mouse.get_pos())
                        positions.append(pygame.mouse.get_pos())
                        tripoints.append(pygame.draw.circle)
                        points.append(pygame.draw.circle)
                        
                    
        if MODE == 2:
            if centre == True and circum == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: #lmb
                        circum = True
                    
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #lmb
                    if centre == True:
                        pass
                    else:           
                        circleindex = len(points)
                        circleposition = pygame.mouse.get_pos()
                        points.append(pygame.draw.circle)
                        positions.append(circleposition)
                        centre = True
                        circum = False
                        circumindex = len(positions)
                        points.append(pygame.draw.circle)
                        circumposition = pygame.mouse.get_pos()
                        positions.append(circumposition)
                          
            
                    
                        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                points = []
                positions = []
                tripoints = []
                tripositions = []
                circlepoints = []
                circlepositions = []
                circumpoints = []
                circumpositions = []
                centre = False
                circum = False
                lockradius = False
                showcircum = False
                showtri = False
                showincircle = False
                lockradius = False
                showtan = False
                outpos = 'N/A'
                outposindex = 'N/A'
            if event.key == pygame.K_t:
                showtri = not showtri
            if event.key == pygame.K_q:
                lockradius = not lockradius
                if lockradius == 0:
                    print('radius unlocked')
                else:
                    print('radius locked')
                xdis = (positions[circumindex])[0] - circleposition[0]
                ydis = (positions[circumindex])[1] - circleposition[1]
            if event.key == pygame.K_w:
                if outpos == 'N/A':
                    outposindex = len(positions)
                    outpos = pygame.mouse.get_pos()
                    points.append(pygame.draw.circle)
                    positions.append(pygame.mouse.get_pos())
            if event.key == pygame.K_i:
                showincircle = not showincircle
            if event.key == pygame.K_c:
                showcircum = not showcircum
            if event.key == pygame.K_1:
                print('triangle mode')
                MODE = 1 #triangle
            if event.key == pygame.K_2:
                print('circle mode')
                MODE = 2 #circle
            if event.key == pygame.K_s:
                showtan = not showtan
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    
    #AXES
    pygame.draw.line(screen,'#A9A9A9',(width/2,0),(width/2,height), 2)
    pygame.draw.line(screen,'#A9A9A9',(0, height/2),(width,height/2), 2)
    
    if len(positions) > 0:
        distances = [distance(pygame.mouse.get_pos(),x) for x in positions]
        closest = min(distances)
        closesti = distances.index(closest)
        if distance(pygame.mouse.get_pos(),positions[closesti]) < radius:
            hoveringi = closesti
            HOVER = True
        else:
            HOVER = False
            
    if lockradius == True:
        positions[circumindex] = (circleposition[0]+xdis,circleposition[1]+ydis)
        
    if HELD:
        if hoveringi == outposindex:
            outpos = pygame.mouse.get_pos()
        if hoveringi == circleindex:
            circleposition = pygame.mouse.get_pos()
        if hoveringi == circumindex:
            circumposition = pygame.mouse.get_pos()
        if positions[hoveringi] in tripositions:
            triposindex = tripositions.index(positions[hoveringi])
            tripositions[triposindex] = pygame.mouse.get_pos()
        positions[hoveringi] = pygame.mouse.get_pos()
        
    if centre == True and circum == False:
        circumposition = pygame.mouse.get_pos()
        positions[circumindex] = pygame.mouse.get_pos()
        
    
    if len(tripoints) == 3:
        lines = [LineSegment(tripositions[0],tripositions[1], showtri),
                 LineSegment(tripositions[1],tripositions[2], showtri),
                 LineSegment(tripositions[2],tripositions[0], showtri)]
        
    if len(tripoints) == 3 and showincircle: 
        lengths = [(distance(tripositions[0],tripositions[1])),
                   (distance(tripositions[1],tripositions[2])),
                   (distance(tripositions[2],tripositions[0]))] 
        T = abs(math.atan(((slope(tripositions[0],tripositions[1]))-(slope(tripositions[1],tripositions[2])))/(1+(slope(tripositions[0],tripositions[1])*(slope(tripositions[1],tripositions[2]))))))
    
        
        Area = (1/2)*lengths[0]*lengths[1]*math.sin(T)
        incentre = [(lengths[0]*tripositions[2][0]+lengths[1]*tripositions[0][0]+lengths[2]*tripositions[1][0])/sum(lengths),
                    (lengths[0]*tripositions[2][1]+lengths[1]*tripositions[0][1]+lengths[2]*tripositions[1][1])/sum(lengths)]
#         pygame.draw.circle(screen,'pink', incentre, radius)
        inradius = (2*Area)/sum(lengths)
        pygame.draw.circle(screen, 'pink',incentre,inradius,3)
    
    
        

    if len(tripoints) == 3 and showcircum:
#         bisectors = [linegeneral(lines[x].M,lines[x].m2) for x in range(3)]
#         circumcentre = simultaneous(bisectors[0],bisectors[1])
#         print(circumcentre)
#         pygame.draw.circle(screen, 'red', circumcentre, radius)

#         lengths = [(distance(positions[0],positions[1])),
#                    (distance(positions[1],positions[2])),
#                    (distance(positions[2],positions[0]))] 
#         A = abs((math.atan(((slope(positions[0],positions[1]))-(slope(positions[0],positions[2])))/(1+(slope(positions[0],positions[1])*(slope(positions[0],positions[2])))))))
#         B = abs((math.atan(((slope(positions[1],positions[0]))-(slope(positions[1],positions[2])))/(1+(slope(positions[1],positions[0])*(slope(positions[1],positions[2])))))))
#         C = abs((math.atan(((slope(positions[2],positions[0]))-(slope(positions[2],positions[1])))/(1+(slope(positions[2],positions[0])*(slope(positions[2],positions[1])))))))
#         angles = [A,B,C]
#         while round(sum(angles), 2) != 3.14:
#             if round(A+B+(math.pi-C),2) == 3.14:
#                 angles = [A,B,(math.pi)-C]
#             elif round(A+(math.pi-B)+C,2) == 3.14:
#                 angles = [A,(math.pi-B),C]
#             elif round((math.pi-A)+B+C,2) == 3.14:
#                 angles = [(math.pi-A),B,C]
#         print(sum(angles))
        
        x1 = tripositions[0][0]
        y1 = tripositions[0][1]
        
        x2 = tripositions[1][0]
        y2 = tripositions[1][1]
        
        x3 = tripositions[2][0]
        y3 = tripositions[2][1]
        
        circumx = ((x1**2+y1**2-x2**2-y2**2)*(y1-y3)-(x1**2+y1**2-x3**2-y3**2)*(y1-y2)) / (2*(x1-x2)*(y1-y3)-2*(x1-x3)*(y1-y2))
        circumy = ((x1-x2)*(x1**2+y1**2-x3**2-y3**2)-(x1-x3)*(x1**2+y1**2-x2**2-y2**2)) / (2*(x1-x2)*(y1-y3)-2*(x1-x3)*(y1-y2))
        circumcentre=(circumx,circumy)
#         pygame.draw.circle(screen, 'red', circumcentre, radius)
        circumradius = distance(tripositions[0],circumcentre)
        pygame.draw.circle(screen, 'red', circumcentre, circumradius, 4)
    
    if centre == True:
        circleradius = distance(positions[circumindex], circleposition)
        pygame.draw.circle(screen, 'white', circleposition, circleradius, 4)
        
    if showtan == True:
        slope1 = (-1*(math.sqrt((outpos[0]**2)*(circleradius**2)+(-2)*(outpos[0])*(circleradius**2)*(circleposition[0])+(outpos[1]**2)*(circleradius**2)+(-2)*(outpos[1])*(circleradius**2)*(circleposition[1])-(circleradius**4)+(circleradius**2)*(circleposition[0]**2)+(circleradius**2)*(circleposition[1]**2))) + (outpos[0]*outpos[1])-(outpos[0]*circleposition[1])-(outpos[1]*circleposition[0])+(circleposition[0]*circleposition[1]) ) / ((outpos[0]**2)+(-2*outpos[0]*circleposition[0])-(circleradius**2)+(circleposition[0]**2))
        slope2 = (1*(math.sqrt((outpos[0]**2)*(circleradius**2)+(-2)*(outpos[0])*(circleradius**2)*(circleposition[0])+(outpos[1]**2)*(circleradius**2)+(-2)*(outpos[1])*(circleradius**2)*(circleposition[1])-(circleradius**4)+(circleradius**2)*(circleposition[0]**2)+(circleradius**2)*(circleposition[1]**2))) + (outpos[0]*outpos[1])-(outpos[0]*circleposition[1])-(outpos[1]*circleposition[0])+(circleposition[0]*circleposition[1]) ) / ((outpos[0]**2)+(-2*outpos[0]*circleposition[0])-(circleradius**2)+(circleposition[0]**2))
        slopes = [slope1,slope2]
        raypoint1 = (outpos[0]-1000,outpos[1]-(slopes[0]*1000))
        raypoint2 = (outpos[0]+1000,outpos[1]+(slopes[0]*1000))
        raypoint3 = (outpos[0]-1000,outpos[1]-(slopes[1]*1000))
        raypoint4 = (outpos[0]+1000,outpos[1]+(slopes[1]*1000))
        pygame.draw.line(screen,'white', raypoint1 ,raypoint2, 4)
        pygame.draw.line(screen,'white', raypoint3 ,raypoint4, 4)

#     print(outpos)
    for i,p in enumerate(points):
        if i == hoveringi:
            p(screen, 'green', positions[i], radius)
        else:
            p(screen, 'white', positions[i], radius)       
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(144)  # fps limit

pygame.quit()