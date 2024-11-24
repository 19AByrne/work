import pygame
import math
# import sympy


##errors / todo
'''
fix reset button - when ran it works but when reset button is clcied and ran again. theorigin of the second motion is at the 240,945 point


'''


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

scale = 20
g = 9.8

initial = (5,10)
savedinitial = initial



xshift = 0
yshift = 0

fontsize = 32
font = pygame.font.Font('freesansbold.ttf', fontsize)

e = 1/2
displayRestitution = ('1/2')

def time(init):
    return ((init[1])) / (4.9)

# def xrange2(init):                  not using this function because it relies on another function
#     return (init[0]) * (time(init))

def xrange(init):
    mag = math.sqrt((init[0])**2+(init[1])**2)
    theta = math.degrees(math.atan(init[1]/init[0]))
    return ( (mag**2) * (math.sin(2*math.radians(theta))) ) / g

def maxheight(init):
    return ( (mag**2) * (math.sin(math.radians(theta)))*(math.sin(math.radians(theta))) ) / (2*g)
    
FireButtonStates = [pygame.image.load('Images/Fire!.png').convert_alpha(),
                    pygame.image.load('Images/Fire! italic.png').convert_alpha(),
                    pygame.image.load('Images/Fire! strike.png').convert_alpha()]
FireButton = FireButtonStates[0]
FireButton_rect = FireButton.get_rect(center=(width/12,height/4))

ResetButton = pygame.image.load('Images/reset.png').convert_alpha()
ResetButton_rect = ResetButton.get_rect(center=(width/12, height/3))

ShowTrailButton_States = [pygame.image.load('Images/ShowTrail.png').convert_alpha(),
                          pygame.image.load('Images/XShowTrail.png').convert_alpha()]
showtrail = True
ShowTrailButton = ShowTrailButton_States[showtrail]
ShowTrailButton_rect = ShowTrailButton.get_rect(center=(width/12,height*7.69/19))

InputterStates = [pygame.image.load('Images/IJ.png').convert_alpha(),
                    pygame.image.load('Images/IJselectedI.png').convert_alpha(),
                    pygame.image.load('Images/IJselectedJ.png').convert_alpha()]
Inputter = InputterStates[0]
Inputter_rect = Inputter.get_rect(center=(width/12,height/7))
I_rect = pygame.Rect(Inputter_rect.left+12,Inputter_rect.top+25, 50, 50)
J_rect = pygame.Rect(Inputter_rect.left+120,Inputter_rect.top+25, 50, 50)

text1 = font.render(str(initial[0]), True, (255,255,255))
text1_rect = text1.get_rect()
text1_rect.center = I_rect.center

text2 = font.render(str(initial[1]), True, (255,255,255))
text2_rect = text2.get_rect()
text2_rect.center = J_rect.center

RestitutionButtonStates = [pygame.image.load('Images/restitution.png').convert_alpha(),
                           pygame.image.load('Images/restitutionSelected.png').convert_alpha()]
inputtingE = False
RestitutionButton = RestitutionButtonStates[inputtingE]
RestitutionButton_rect = RestitutionButton.get_rect(center = (width/12,height*8.09/17))

Bounce = False
BounceButtonStates = [pygame.image.load('Images/Bounce.png').convert_alpha(),
                      pygame.image.load('Images/XBounce.png').convert_alpha()]
BounceButton = BounceButtonStates[Bounce]
BounceButton_rect = BounceButton.get_rect(center=(width/12, height*8.09/17 + 77))

landing = pygame.event.custom_type()
scaleshift = pygame.event.custom_type()
scaleshiftevent = pygame.event.Event(scaleshift)
simulating = False
landed = False
originstate = True
path = []
rawpath = []
initials = [initial]
ranges = []

totalT = 0
inputting = False

bounceCount = 0
maxBounce = 1

inputtinga = False
inputtingb = False
inputReady = False



def fire(initial, deltaTime, gravity,origin,scale, bc):
    t = deltaTime/1000
#     x = origin[0] + (initial[0]*t) * scale
#     y = origin[1] - ( (initial[1]*t) - (gravity/2)*(t**2) ) * scale
    
    x = (initial[0]*t)
    y = ( (initial[1]*t) - (gravity/2)*(t**2) )
    return [origin, (x,y), xrange(initial)*bc]

class Motion:
    def __init__(self, initial, origin, range, totaltime, gravity, motionNo):
        self.initial = initial
        self.initialx = self.initial[0]
        self.initialy = self.initial[1]
        self.range = range
        self.origin = origin
        self.originx = self.origin[0]
        self.totalT = totaltime
        self.gravity = gravity
        self.motionNo = motionNo
        
    def getpoint(self, deltaTime):
        deltaTime = deltaTime/1000
        x = (self.initialx*deltaTime)
        y = (self.initialy*deltaTime) - (self.gravity/2)*(deltaTime**2)
        return [(x,y), self.range, self.motionNo]
    
    
origins = []

motions = []
origin = (width/8, height*7/8)
originlist = [origin]

while running:

    text1 = font.render(str(savedinitial[0]), True, (255,255,255))
    text1_rect = text1.get_rect()
    text1_rect.center = I_rect.center
    text2 = font.render(str(savedinitial[1]), True, (255,255,255))
    text2_rect = text2.get_rect()
    text2_rect.center = J_rect.center
    
    ############# for debugging
    BOUNCECOUNT = font.render(str(bounceCount), True, (255,255,255))

    
    Restitution_text = font.render(displayRestitution, True, (255,255,255))
    Restitution_text_rect = Restitution_text.get_rect()
    Restitution_text_rect.center = (RestitutionButton_rect.center[0]+55,RestitutionButton_rect.center[1]+2)
    
    dT = clock.get_time()
    
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if FireButton_rect.collidepoint(event.pos):
                if not simulating and originstate:
                    pygame.time.set_timer(landing, round(time(initial)*1000), 1)
                    motions.append(Motion(initial, origin, xrange(initial), time(initial), g, 0))
                    simulating = True
                    originstate = False
                    
            if ResetButton_rect.collidepoint(event.pos):
                simulating = False
                landed = False
                originstate = True
                totalT = 0
                path = []
                rawpath = []
                initials = [initial]
                ranges = []
                origins = []
                originlist = [origin]
                origin = (width/8, height*7/8)
                bounceCount = 0
                initial = savedinitial
                motions = []
                
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
            if BounceButton_rect.collidepoint(event.pos):
                Bounce = not Bounce
            if RestitutionButton_rect.collidepoint(event.pos):
                inputtingE = True
                inputtinga = True
                a = ''
                b = ''                
                
        if event.type == pygame.KEYDOWN:
            if inputting and originstate:
                if event.key >= 48 and event.key <= 57:
                    emptyvalue = emptyvalue + str(pygame.key.name(event.key))
                if event.key == pygame.K_PERIOD:
                    emptyvalue = emptyvalue + str(pygame.key.name(event.key))
                if event.key == pygame.K_BACKSPACE:
                    emptyvalue = emptyvalue[:-1]
                if event.key == pygame.K_RETURN:
                    if emptyvalue == '':
                        emptyvalue ='0.000000000000000001'
                    if selected == 'i':
                        if float(emptyvalue) == int(emptyvalue):
                            initial = ( int(emptyvalue), initial[1] )
                        else:
                            initial = ( float(emptyvalue), initial[1] )
                    if selected == 'j':
                        if float(emptyvalue) == int(emptyvalue):
                            initial = ( initial[0], int(emptyvalue) )
                        else:
                            initial = ( initial[0], float(emptyvalue) )
                    savedinitial = initial
                    inputting = False

            if inputtingE and originstate:                
                if event.key >= 48 and event.key <= 57:
                    if inputtinga:
                        a = str(pygame.key.name(event.key))
                    if inputtingb:
                        b = str(pygame.key.name(event.key))
                if event.key == pygame.K_SLASH:
                    if a != '':
                        inputtinga = False
                        inputtingb = True
                if b != '':
                    inputReady = True
                if event.key == pygame.K_RETURN and inputReady:
                    e = int(a)/int(b)
                    print(a)
                    print(b)
                    displayRestitution = (f'{a}/{b}')
                    inputtingE = False
                    
                    
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
                    xshift -= 10
#             if event.key == pygame.K_i or event.key == pygame.K_o:
                
            if event.key == pygame.K_i:
                scale += 0.25
            if event.key == pygame.K_o:
                scale -= 0.25
                
            if event.key == pygame.K_r:
                xshift, yshift = 0,0
                scale = 20
                
            ####keys to be turned into buttons               
    
        if event.type == scaleshift:
            ranges = [scale*xrange(init) for init in initials]
            
            origins = []
            for i,r in enumerate(ranges):
                if i == 0:
                    origins.append(r)
                else:
                    origins.append(origins[i-1]+r)
            origins = [o+240 for o in origins]
            origins.insert(0,240)
            path = [[(scale*p[0][0],scale*p[0][1]),(p[1]), p[2]] for i,p in enumerate(rawpath)]


            

        if event.type == landing and simulating:
            if not Bounce:
                simulating = False
                landed = True
            else:
                bounceCount += 1

                initial = (initial[0], (e)*initial[1])
                initials.append(initial)
                if bounceCount >= 1:
                    originlist.append(origin)
                    motions.append(Motion(initial, (0,0), xrange(initial), time(initial), g, bounceCount))
                
                totalT = 0
                if initial[1] < 0.05:  #THIS VALUE SHOULD BE MUCH LOWER I HAVE BEEN USING 'initial[1] < 0.05' AS WHEN IT GTS BELOW THAT SPEED IT IS JUST AN UNNECESARY PROCESS. THE LARGER VALUE IS PURELY FOR DEBUGGING
                    simulating = False
                    landed = True
                else:
                    pygame.time.set_timer(landing, round(time(initial)*1000), 1)

                

    screen.fill("black")
    
    ground = pygame.Rect(0 , (height*7/8) - yshift ,width,height/8)
    pygame.draw.rect(screen, 'dark green', ground) #ground
    
    for x in range(100):
        pygame.draw.circle(screen, 'blue', (width/8 + x*scale -xshift, (height*7/8) - yshift), 3)
        
    if simulating:
        mousepos = pygame.mouse.get_pos()
        if FireButton_rect.collidepoint(mousepos):
            FireButton = FireButtonStates[2]
        else:
            FireButton = FireButtonStates[1]
        totalT += dT
        path.append(motions[bounceCount].getpoint(totalT))
        rawpath.append(motions[bounceCount].getpoint(totalT))
        if totalT >= time(initial)*1000 and not Bounce:
            simulating = False
        
    
    if originstate:
        FireButton = FireButtonStates[0]
    else:
        if showtrail:
            for p in path[:-1]:
                if bounceCount == 0:
                    pygame.draw.circle(screen, 'white', (240 + p[0][0] - xshift,origin[1] - p[0][1] - yshift), 3)
                else:
                    pygame.draw.circle(screen, 'white', (origins[p[2]] + p[0][0] - xshift,origin[1] - p[0][1] - yshift), 3)
            
            
            
            
            
            
            
#             for i,p in enumerate(path[:-1]): #FILTERING OUT LATEST POINT AS IT CANT BE SCALED CORRECTLY IN TIME FOR DISPLAY.FLIP
#                 if bounceCount >= 1:
#                     pass
#                     pygame.draw.circle(screen, 'white', (origin[0] + p[0][0] - xshift ,origin[1] - p[0][1] - yshift), 3)
#                 else:
#                     pass
#                     pygame.draw.circle(screen, 'pink', (origin[0] + p[0][0] - xshift ,origin[1] - p[0][1] - yshift), 3)
#             if totalT > (time(initial)*1000)/2:
#                 pygame.draw.circle(screen, 'red', (origin[0] + (xrange(initial))/2 - xshift,  origin[1] - maxheight(initial) - yshift), 5)
#             if totalT >= (time(initial)*1000):
#                 pygame.draw.circle(screen, 'orange', (origin[0] + xrange(initial) - xshift, origin[1] - yshift), 5)
#         if not showtrail and totalT < (time(initial)*1000):
#             currentpos = fire(initial, totalT, g, origin, scale, bounceCount)[1]
#             pygame.draw.circle(screen, 'purple',(origin[0] + currentpos[0] - xshift,origin[1] - currentpos[1] - yshift) , 3)
    pygame.event.post(scaleshiftevent)


    pygame.draw.circle(screen, 'red', (origin[0]-xshift,origin[1]-yshift), 5) # origin

    screen.blit(FireButton,FireButton_rect)
    screen.blit(ResetButton, ResetButton_rect)
    screen.blit(ShowTrailButton, ShowTrailButton_rect)
    screen.blit(Inputter,Inputter_rect)
    screen.blit(RestitutionButtonStates[inputtingE], RestitutionButton_rect)
    screen.blit(Restitution_text,Restitution_text_rect)
    if not inputting:
        Inputter = InputterStates[0]
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
    screen.blit(BounceButtonStates[Bounce],BounceButton_rect)
    

    ###
    screen.blit(BOUNCECOUNT,(width/2,height/2))
#     pygame.draw.circle(screen, 'brown', (240 + scale*xrange(initial),945), 10)
    pygame.display.flip()
    clock.tick(144)  # fps limit










