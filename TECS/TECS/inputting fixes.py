import pygame
import math
#what to know
'''
All images were created by me
All code was written by me, concept of deltaTime was introduced to me by mentor but applied to code with my own interpretation of its use
Formulas such as max height,time, and range are formulas derived in the applied maths LC course

Keyboard inputs are:
    i - zoom in
    o - zoom out
    [arrow keys] - move screen in respective direction
    r - resets any changes to the screen view (offset or zoom)
    Escape - Closes the window

    inputting restition is single digit number followed by '/' and single digit number
    return key is then pressed to confirm the value

    I J values can be any positive number followed by return key to confirm the value

'''

##errors / to-do
'''
i kinda did mag angle switching but its buggy with number 13 so probably a lot more. honestly i could just make the value clear when switching if neccasary

the firebutton cross state can only change during the motion and cannot be changed when landed and not in originstate
perhaps move the lines of code

when entering 0 in inputter it causes zerodiv error

other box can be selected before finished editing other box

BLUE DOTS ARE NOT 10M APART

TIMES NOT ACCURATE IN TOP RIGHT 
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

initial = (5,5) #default initial value
savedinitial = initial #saving the initial so as it changes due to impact it reverts back to the user selected input when reset put is clicked

xshift = 0 # offset in the x-axis used with left and arrow keys
yshift = 0 # offset in the y-axis used with up and down arrow keys
#both offsets are applied to all coordinates of points

fontsize = 32
font = pygame.font.Font('freesansbold.ttf', fontsize)


e = 1/2 #value for restitution, denoted with e in applied maths
displayRestitution = ('1/2') #string of value for e for 

def time(init):
    return ((init[1])) / (4.9)

def xrange(init): #horizontal distance covered in a motion
    mag = math.sqrt((init[0])**2+(init[1])**2) #magnitude of velocity
    theta = math.degrees(math.atan(init[1]/init[0])) #angle particle is projected at
    return ( (mag**2) * (math.sin(2*math.radians(theta))) ) / g

def maxheight(init):
    
    return ( (mag**2) * (math.sin(math.radians(theta)))*(math.sin(math.radians(theta))) ) / (2*g)





###declaring all the images and their required states/rects
FireButtonStates = [pygame.image.load('Images/Fire!.png').convert_alpha(),
                    pygame.image.load('Images/Fire! italic.png').convert_alpha(),
                    pygame.image.load('Images/Fire! strike.png').convert_alpha()]#list of different states for ready to fire, in motion, or Cross through it while hovering to say you can't press
FireButton = FireButtonStates[0]
FireButton_rect = FireButton.get_rect(center=(width/12,height/4))

ResetButton = pygame.image.load('Images/reset.png').convert_alpha()
ResetButton_rect = ResetButton.get_rect(center=(width/12, height/3))

ShowTrailButton_States = [pygame.image.load('Images/ShowTrail.png').convert_alpha(),
                          pygame.image.load('Images/XShowTrail.png').convert_alpha()]
showtrail = False
ShowTrailButton = ShowTrailButton_States[showtrail]
ShowTrailButton_rect = ShowTrailButton.get_rect(center=(width/12,height*7.69/19))

InputterStates = [pygame.image.load('Images/Inputter.png').convert_alpha(),
                    pygame.image.load('Images/InputterBox1selected.png').convert_alpha(),
                    pygame.image.load('Images/InputterBox2selected.png').convert_alpha()]
Inputter = InputterStates[0]
Inputter_rect = Inputter.get_rect(center=(width/12,height/7))
I_rect = pygame.Rect(Inputter_rect.left+12,Inputter_rect.top+25, 50, 50)
J_rect = pygame.Rect(Inputter_rect.left+120,Inputter_rect.top+25, 50, 50)
IJmode = True

OverlayStates = [pygame.image.load('Images/MDoverlay.png').convert_alpha(),
                 pygame.image.load('Images/IJoverlay.png').convert_alpha()]
Overlay = OverlayStates[IJmode] 

SwitchButton = pygame.image.load('Images/Switch.png').convert_alpha()
SwitchButton_rect = SwitchButton.get_rect()
SwitchButton_rect.center = (Inputter_rect.center[0]+110,Inputter_rect.center[1])

displayValueBox1 = ''
displayI_Value = font.render(displayValueBox1, True, (255,255,255))
displayI_Value_rect = displayI_Value.get_rect()
displayI_Value_rect.center = I_rect.center

displayValueBox2 = ''
displayJ_Value = font.render(displayValueBox2, True, (255,255,255))
displayJ_Value_rect = displayJ_Value.get_rect()
displayJ_Value_rect.center = J_rect.center

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

BlankBox = pygame.image.load('Images/BlankBox.png').convert_alpha()
baseBlankBox_rect = BlankBox.get_rect(center=(width-105,45))

NeedHelp = False
HelpButton = pygame.image.load('Images/Help.png').convert_alpha()
HelpButton_rect = HelpButton.get_rect(center=(width-60,height-60))
HelpMenu = pygame.image.load('Images/HelpMenu.png').convert_alpha()


######
HideButton = pygame.image.load('Images/EYEPICTUREDOBETTER.png').convert_alpha()
HideButton_rect = HideButton.get_rect(topleft=(0,0))
HideUI = False

landing = pygame.event.custom_type()

#custom event for when zoomed in or out, to multiply coordinates by the variable scale
scaleshift = pygame.event.custom_type()
scaleshiftevent = pygame.event.Event(scaleshift) 

simulating = False
landed = False
originstate = False #origin state is basically a ready to fire state, its to differentiate if the projectile is not in motion but its still active and not ready to fire to the projectile not being in motion and being in a ready to fire state
boolListValues = [0,0]
path = [] #list for points of the motion with scale applied
rawpath = [] #raw list of the points without scale applied so the points can be changed upon the scaleshiftevent
initials = [initial] #list of initials
ranges = [] #list of each range of seperate motion

totalT = 0
displayTimeValue = 0 #true total time value of entire motion to be displayed to user
inputting = False

bounceCount = 0

inputtinga = False
inputtingb = False
inputReady = False


########################################################################################
fakeinitial = initial

def currentpoint(initial, deltaTime, gravity): #function to give any coordinate of a motion at any time.
    t = deltaTime/1000    
    x = (initial[0]*t)
    y = ( (initial[1]*t) - (gravity/2)*(t**2) )
    return (x,y)

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
    
Points = []
class Point:
    def __init__(self, displayCoordinate, realCoordinate):
        self.displayCoordinate = displayCoordinate
        self.realCoordinate = realCoordinate
    
    def update(self):
        pygame.draw.circle(screen, 'purple', displayCoordinate, 5)
    
origins = []
motions = []
origin = (width/8, height*7/8) #True Origin point
originlist = [origin]

displayTime = font.render(f'{round(displayTimeValue/1000,1)}s', True, (255,255,255)) #here twice to be initialised
displayTime_rect = displayTime.get_rect()
displayTime_rect.center = baseBlankBox_rect.center

displayXrange = font.render(f'{round((displayTimeValue/1000)*savedinitial[0],1)}m', True, (255,255,255))
displayXrange_rect = displayXrange.get_rect()
displayXrange_rect.center = (baseBlankBox_rect.center[0],baseBlankBox_rect.center[1]+77)

displayBounceCount = font.render(f'Bounces: {bounceCount}' , True, (255,255,255))
displayBounceCount_rect = displayBounceCount.get_rect()
displayBounceCount_rect.center = (baseBlankBox_rect.center[0],baseBlankBox_rect.center[1]+154)

while running:
    if not inputting:
        if IJmode:
            if boolListValues[0] == 1:
                displayValueBox1 = str(savedinitial[0])
            if boolListValues[1] == 1:
                displayValueBox2 = str(savedinitial[1])
        else:
            if boolListValues[0] == 1:
                ddisplayValueBox1 = str(round(math.sqrt((savedinitial[0]**2)+(savedinitial[1]**2)),2))
            if boolListValues[1] == 1:
                displayValueBox2 = str(round(math.degrees(math.atan(savedinitial[1]/savedinitial[0])),1))
    
    dT = clock.get_time() #deltaTime
    displayI_Value = font.render(displayValueBox1, True, (255,255,255))
    displayI_Value_rect = displayI_Value.get_rect()
    displayI_Value_rect.center = I_rect.center
    displayJ_Value = font.render(displayValueBox2, True, (255,255,255))
    displayJ_Value_rect = displayJ_Value.get_rect()
    displayJ_Value_rect.center = J_rect.center
    
    #Information boxes of the motion in the top right, inside game loop so text can update
    displayBounceCount = font.render(f'Bounces: {bounceCount}' , True, (255,255,255)) 
    displayTime = font.render(f'{round(displayTimeValue/1000,1)}s', True, (255,255,255))
    displayXrange = font.render(f'{round((displayTimeValue/1000)*savedinitial[0],1)}m', True, (255,255,255))
    
    Restitution_text = font.render(displayRestitution, True, (255,255,255))
    Restitution_text_rect = Restitution_text.get_rect()
    Restitution_text_rect.center = (RestitutionButton_rect.center[0]+55,RestitutionButton_rect.center[1]+2)
    
    
    MOUSECOORDS = font.render(str(pygame.mouse.get_pos()), True, (255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not HideUI:
            if FireButton_rect.collidepoint(event.pos):
                if not simulating and originstate: #only fires when in a ready to fire state
                    pygame.time.set_timer(landing, round(time(initial)*1000), 1)
                    motions.append(Motion(initial, origin, xrange(initial), time(initial), g, 0))
                    simulating = True
                    originstate = False
                    
            if ResetButton_rect.collidepoint(event.pos):
                #resets all values to default value
                simulating = False
                landed = False
                if all(boolListValues):
                    originstate = True
                totalT = 0
                displayTimeValue = 0
                path = []
                rawpath = []
                initials = [savedinitial]
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
                if originstate or not all(boolListValues):
                    Inputter = InputterStates[1]
                    inputting = True
                    selected = 0
                    displayWorkingValue = ''
                    
            if J_rect.collidepoint(event.pos):
                if originstate or not all(boolListValues):
                    Inputter = InputterStates[2]
                    inputting = True
                    selected = 1
                    displayWorkingValue = ''
                    
            if SwitchButton_rect.collidepoint(event.pos):
                if originstate or not all(boolListValues):
                    IJmode = not IJmode #reverses bool value
                    Overlay = OverlayStates[IJmode]
                    boolListValues = [0,0]
                    originstate = False
                    displayValueBox1 = ''
                    displayValueBox2 = ''
                
                
            if BounceButton_rect.collidepoint(event.pos):
                Bounce = not Bounce #reverses bool value
                
            if RestitutionButton_rect.collidepoint(event.pos):
                if originstate or not all(boolListValues):
                    inputtingE = True
                    workingRestitution = ''
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if HideButton_rect.collidepoint(event.pos):
                HideUI = not HideUI
                
        if event.type == pygame.KEYDOWN:
            if inputting:
                if event.key >= 48 and event.key <= 57: #48-57 is the relative key for 0-9 
                    displayWorkingValue = displayWorkingValue + str(pygame.key.name(event.key))
                if event.key == pygame.K_PERIOD:
                    displayWorkingValue = displayWorkingValue + str(pygame.key.name(event.key))
                if event.key == pygame.K_BACKSPACE:
                    displayWorkingValue = displayWorkingValue[:-1] #deletes last value of str
                if event.key == pygame.K_RETURN and not not displayWorkingValue: #(not str) returns True if the str is empty therefore (not not str) returns False if the str is empty
                    if IJmode:
                        if selected == 0:
                            try:
                                initial = ( int(displayWorkingValue), initial[1] ) 
                            except:
                                initial = ( float(displayWorkingValue), initial[1] )
                        if selected == 1:
                            try:
                                initial = ( initial[0], int(displayWorkingValue) ) 
                            except:
                                initial = ( initial[0], float(displayWorkingValue) )
                                
                    if not IJmode:
                        if selected == 0:
                            try:
                                fakeinitial = ( int(displayWorkingValue), fakeinitial[1] ) 
                            except:
                                fakeinitial = ( float(displayWorkingValue), fakeinitial[1] )
                        if selected == 1:
                            try:
                                fakeinitial = ( fakeinitial[0], int(displayWorkingValue) ) 
                            except:
                                fakeinitial = ( fakeinitial[0], float(displayWorkingValue) )   
                        initial = ( round(fakeinitial[0]*math.cos(math.radians(fakeinitial[1])),2), round(fakeinitial[0]*math.sin(math.radians(fakeinitial[1])),2))
                    savedinitial = initial
                    initials = [savedinitial]
                    boolListValues[selected] = 1
                    inputting = False
                    if all(boolListValues): 
                        originstate = True
                
            if inputtingE:
                if event.key >= 48 and event.key <= 57: #1-9
                    workingRestitution = workingRestitution + str(pygame.key.name(event.key))
                if event.key == pygame.K_SLASH:
                    workingRestitution = workingRestitution + str(pygame.key.name(event.key))
                if event.key == pygame.K_BACKSPACE:
                    workingRestitution = workingRestitution[:-1] #deletes last value of str
                if event.key == pygame.K_RETURN and len(workingRestitution.strip('/')) >= 3 and '/' in workingRestitution.strip('/') and workingRestitution.count('/') == 1 and len(workingRestitution.strip('0')) >= 3:
                    inputtingE = False
                    a = int(workingRestitution[:workingRestitution.find('/')])
                    b = int(workingRestitution[workingRestitution.find('/')+1:])
                    e = a/b
                    
            if event.key == pygame.K_ESCAPE:
                running = False
                
            if event.key == pygame.K_UP:
                yshift -= 10
                
            if event.key == pygame.K_DOWN: #limits the yshift so it cannot go more down then needed
                if yshift != 0:
                    yshift += 10
                    
            if event.key == pygame.K_RIGHT:
                xshift += 10
                
            if event.key == pygame.K_LEFT:#limits the xshift so it cannot go more left then needed
                if xshift != 0:
                    xshift -= 10
                
            if event.key == pygame.K_i:
                scale += 0.25
                
            if event.key == pygame.K_o:
                if scale != 0.25: #limiting scale
                    scale -= 0.25
                
            if event.key == pygame.K_r: #resets offset and scale
                xshift, yshift = 0,0
                scale = 20            

        if event.type == scaleshift: #event called to adjust the coordinate points to the requried scale
            ranges = [scale*xrange(init) for init in initials]
            
            origins = [] #resets the origin list as it needs to be updated according to the range of each motion to adjust for scale
            for i,r in enumerate(ranges):
                if i == 0: 
                    origins.append(r) #____________________
                else:
                    origins.append(origins[i-1]+r) #____________________
            origins = [o+(width/8) for o in origins] #accounting for offset of the True origin point
            origins.insert(0,(width/8)) #inserts the True origin point in the list
            path = [[(scale*p[0][0],scale*p[0][1]),(p[1]), p[2]] for i,p in enumerate(rawpath)] #____________________

        if event.type == landing and simulating:
            if not Bounce:
                simulating = False
                landed = True
            else:
                bounceCount += 1
                initial = (initial[0], (e)*initial[1]) 
                '''
                applies restituion to the velocity when particle hits the floor,
                it can be applied to the initial as the motion is on a horizontal plane,
                so the final velocity is always (initial[0], -initial[1]) because its a perfectly mirrored motion,
                knowing this lets me not use the formula '-e = v/u' and the need to go through the trouble of solving for final velocity
                allowing me to simply multiply the (initial[1] * e)
                '''
                initials.append(initial)
#                 if bounceCount >= 1:
#                     motions.append(Motion(initial, (0,0), xrange(initial), time(initial), g, bounceCount))
                motions.append(Motion(initial, (0,0), xrange(initial), time(initial), g, bounceCount)) #for myself, the if statement seemed unnecasary, if any issues may arise investigate if its needed
                
                
                totalT = 0 #resets the time to be used for new motion
                if initial[1] < 0.05:
                    #caps the y-value. When the Y-velocity is uncapped because its being reduced by a fraction it can never reach 0. therefor infinite bounce.
                    #this only happens in this simulation as it cannot truly account for eveyr acting force on the particle
                    simulating = False
                    landed = True
                else:
                    pygame.time.set_timer(landing, round(time(initial)*1000), 1) #starts a new timer of the time of the new motion with its new velocity

    screen.fill("black")
    
    ground = pygame.Rect(0 , (height*7/8) - yshift ,width,height/8)
    pygame.draw.rect(screen, 'dark green', ground) #ground
    
    for x in range(100):
        pygame.draw.circle(screen, 'blue', (width/8 + x*scale -xshift, (height*7/8) - yshift), 3)#Blue points, (places exactly 10m apart)
        
    mousepos = pygame.mouse.get_pos()    
    if HelpButton_rect.collidepoint(mousepos):
        NeedHelp = True
    else:
        NeedHelp = False
    
    
    if simulating:
        totalT += dT
        displayTimeValue += dT
        path.append(motions[bounceCount].getpoint(totalT))
        rawpath.append(motions[bounceCount].getpoint(totalT))
        if totalT >= time(initial)*1000 and not Bounce:
            simulating = False
        
    if not originstate:
        if FireButton_rect.collidepoint(mousepos): #Checking if hovering over the button,
            FireButton = FireButtonStates[2] #changes the state of the button to visually diplay to user it cannot currently be pressed
        else:
            FireButton = FireButtonStates[1]
            
    if inputting:
        if selected == 0:
            displayValueBox1 = displayWorkingValue
        else:
            displayValueBox2 = displayWorkingValue
    
    if inputtingE:
#         print(workingRestitution)
        displayRestitution = workingRestitution
#         print(displayRestitution)
    
    if originstate:
        FireButton = FireButtonStates[0]
    elif all(boolListValues):
        #Y-value for coordinates of origin points will always be the same as the True Origin points y-value, allowing me to call origin[1]
        if showtrail:
            for p in path[:-1]: #Filtering out latest point in list as it cannot be scaled fast enough
                '''
                p[2] is taken form the motion.getpoint(...) function, it is the motion Number.
                It is used so I can index the origins list and it will correctly use the correct offset when iterating through the path,
                as each point in the path has a origin assigned it it
                '''
                pygame.draw.circle(screen, 'white', (origins[p[2]] + p[0][0] - xshift,origin[1] - p[0][1] - yshift), 3)
                
        if not showtrail and totalT < (time(initial)*1000):
            '''
            if not showing trail, the entire path does not need to be kept track of, so I can just calculate the point at the exact current time,
            indexing origins with the bounceCount as the bounceCount cannot go down but I wouldnt need to render any past motions.
            '''
            currentpos = currentpoint(initial, totalT, g)
            pygame.draw.circle(screen, 'white', (origins[bounceCount] +  currentpos[0]*scale - xshift,origin[1] - currentpos[1]*scale - yshift), 3)
#             if totalT > (time(initial)*1000)/2:
#                 pygame.draw.circle(screen, 'red', (origin[0] + (xrange(initial))/2 - xshift,  origin[1] - maxheight(initial) - yshift), 5)
#             if totalT >= (time(initial)*1000):
#                 pygame.draw.circle(screen, 'orange', (origin[0] + xrange(initial) - xshift, origin[1] - yshift), 5)
#         if not showtrail and totalT < (time(initial)*1000):
#             currentpos = fire(initial, totalT, g, origin, scale, bounceCount)[1]
#             pygame.draw.circle(screen, 'purple',(origin[0] + currentpos[0] - xshift,origin[1] - currentpos[1] - yshift) , 3)
    pygame.event.post(scaleshiftevent)

    pygame.draw.circle(screen, 'red', (origin[0]-xshift,origin[1]-yshift), 5) # True Origin
    
    ##testing classes
#     for o in origins:
#         print(o)
    
    
    
    if not HideUI:
        #information boxes in top right
        screen.blit(BlankBox,baseBlankBox_rect)
        screen.blit(BlankBox,(baseBlankBox_rect[0],baseBlankBox_rect[1]+77))
        screen.blit(BlankBox,(baseBlankBox_rect[0],baseBlankBox_rect[1]+154))
        
        #information values in top right
        screen.blit(displayTime,displayTime_rect) 
        screen.blit(displayXrange,displayXrange_rect)
        screen.blit(displayBounceCount,displayBounceCount_rect)
        
        #buttons for user and their values
        screen.blit(FireButton,FireButton_rect)
        screen.blit(ResetButton, ResetButton_rect)
        screen.blit(ShowTrailButton, ShowTrailButton_rect)
        
        if not inputting:
            Inputter = InputterStates[0]
        screen.blit(Inputter,Inputter_rect)
        screen.blit(Overlay,Inputter_rect)
        
        screen.blit(SwitchButton,SwitchButton_rect)
        screen.blit(RestitutionButtonStates[inputtingE], RestitutionButton_rect)
        screen.blit(Restitution_text,Restitution_text_rect)
        


        screen.blit(displayI_Value, displayI_Value_rect)
        screen.blit(displayJ_Value, displayJ_Value_rect)        
        screen.blit(BounceButtonStates[Bounce],BounceButton_rect)
        screen.blit(HelpButton,HelpButton_rect)
        if NeedHelp:
            screen.blit(HelpMenu,(0,0))



    screen.blit(HideButton,HideButton_rect)
    screen.blit(MOUSECOORDS, mousepos)

    pygame.display.flip()
    clock.tick(144)  # fps limit

pygame.quit()








