# Example file showing a basic pygame "game loop"
import pygame
import math

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


HOVER = False
HELD = False
showtri = False
showincircle = False
showcircum = False

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
            if event.key == pygame.K_c:
                showcircum = not showcircum
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
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
            
    if HELD:
        positions[hoveringi] = pygame.mouse.get_pos()
    
    if len(points) == 3:
        lines = [LineSegment(positions[0],positions[1], showtri),
                 LineSegment(positions[1],positions[2], showtri),
                 LineSegment(positions[2],positions[0], showtri)]
        
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
        

    if len(points) == 3 and showcircum:
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
#         
        x1 = positions[0][0]
        y1 = positions[0][1]
        
        x2 = positions[1][0]
        y2 = positions[1][1]
        
        x3 = positions[2][0]
        y3 = positions[2][1]
        
        circumx = ((x1**2+y1**2-x2**2-y2**2)*(y1-y3)-(x1**2+y1**2-x3**2-y3**2)*(y1-y2)) / (2*(x1-x2)*(y1-y3)-2*(x1-x3)*(y1-y2))
        circumy = ((x1-x2)*(x1**2+y1**2-x3**2-y3**2)-(x1-x3)*(x1**2+y1**2-x2**2-y2**2)) / (2*(x1-x2)*(y1-y3)-2*(x1-x3)*(y1-y2))
        circumcentre=(circumx,circumy)
#         pygame.draw.circle(screen, 'red', circumcentre, radius)
        circumradius = distance(positions[0],circumcentre)
        pygame.draw.circle(screen, 'red', circumcentre, circumradius, 4)   
        
    for i,p in enumerate(points):
        if i == hoveringi:
            p(screen, 'green', positions[i], radius)
        else:
            p(screen, 'white', positions[i], radius)       
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()