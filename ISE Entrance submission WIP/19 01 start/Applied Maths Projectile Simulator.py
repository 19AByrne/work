import pygame
import math

#what to know
'''
All images were created by me, Aaron Byrne.
All code was written by me, concept of deltaTime was introduced to me by mentor but applied to code with my own interpretation of its use
Formulas such as max height,time, and range are formulas derived in the applied maths LC course
Some may have been my own logical interpretation of them.
Countless tests on paper of the motions were performed by myself while coding the actual solving of any value for the motion such as time and maxheight etc.
'''

##errors / to-do
'''
display info values for range do not exactly match the final point coordinates when displayed, possibly deltaTime issue.

dont forget about vertical lines
there is a unknown random value being appended to origins at the end of motions with bounce, too tired to deal with it rn and its not bothering me
i need to find a way to change how finalpoint is calculted cos when its at 0 it says -0.03m which is just tragic to look at
'''


pygame.init()
wh = pygame.display.get_desktop_sizes()[0]
height = wh[1]
width = wh[0]
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

scale = 20 #default scale value
g = 9.8 #gravity

initial = (5,5) #default initial value
savedinitial = initial #saving the initial so as it changes due to restitution it reverts back to the user selected input when reset button is clicked

xshift = 0 # offset in the x-axis used with left and arrow keys
yshift = 0 # offset in the y-axis used with up and down arrow keys
#both offsets are applied to all coordinates of points

fontsize = 32
font = pygame.font.Font('freesansbold.ttf', fontsize)
debugfont = pygame.font.Font('freesansbold.ttf', 16)


e = 1/2 #value for restitution, denoted with e in applied maths
displayRestitution = ('1/2') #string of value for e for 

def time(init): #gets the time of a single motion
    return ((init[1])) / (4.9)

def xrange(init): #horizontal distance covered in a motion
    mag = math.sqrt((init[0])**2+(init[1])**2) #magnitude of velocity
    theta = math.degrees(math.atan(init[1]/init[0])) #angle particle is projected at
    return ( (mag**2) * (math.sin(2*math.radians(theta))) ) / g

def maxheight(init): #maximum height reached in a single motion
    mag = math.sqrt((init[0])**2+(init[1])**2) #magnitude of velocity
    theta = math.degrees(math.atan(init[1]/init[0])) #angle particle is projected at
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
ShowTrailButton = ShowTrailButton_States[showtrail] #showtrail is bool therefore can be used to index its states
ShowTrailButton_rect = ShowTrailButton.get_rect(center=(width/12,height*7.69/19))

InputterStates = [pygame.image.load('Images/Inputter.png').convert_alpha(),
                    pygame.image.load('Images/InputterBox1selected.png').convert_alpha(),
                    pygame.image.load('Images/InputterBox2selected.png').convert_alpha()]
Inputter = InputterStates[0]
Inputter_rect = Inputter.get_rect(center=(width/12,height/7))
Box1_rect = pygame.Rect(Inputter_rect.left+12,Inputter_rect.top+25, 50, 50)
Box2_rect = pygame.Rect(Inputter_rect.left+120,Inputter_rect.top+25, 50, 50)
IJmode = True
inputting = False

OverlayStates = [pygame.image.load('Images/MDoverlay.png').convert_alpha(), #overalys showing the unit depending on which mode you are in. mag & angle or I & J.
                 pygame.image.load('Images/IJoverlay.png').convert_alpha()]
Overlay = OverlayStates[IJmode] #bool value to index 

SwitchButton = pygame.image.load('Images/Switch.png').convert_alpha() #switch button for switching IJmode
SwitchButton_rect = SwitchButton.get_rect()
SwitchButton_rect.center = (Inputter_rect.center[0]+110,Inputter_rect.center[1])

displayValueBox1 = ''
displayBox1Text = font.render(displayValueBox1, True, (255,255,255))
displayBox1Text_rect = displayBox1Text.get_rect()
displayBox1Text_rect.center = Box1_rect.center

displayValueBox2 = ''
displayBox2Text = font.render(displayValueBox2, True, (255,255,255))
displayBox2Text_rect = displayBox2Text.get_rect()
displayBox2Text_rect.center = Box2_rect.center

testTextValue = 0
testText = font.render(str(testTextValue), True, (255,255,255))

RestitutionButtonStates = [pygame.image.load('Images/restitution.png').convert_alpha(),
                           pygame.image.load('Images/restitutionSelected.png').convert_alpha()]
inputtingE = False
RestitutionButton = RestitutionButtonStates[inputtingE]#bool value to index
RestitutionButton_rect = RestitutionButton.get_rect(center = (width/12,height*8.09/17))

Bounce = False
BounceButtonStates = [pygame.image.load('Images/Bounce.png').convert_alpha(),
                      pygame.image.load('Images/XBounce.png').convert_alpha()]
BounceButton = BounceButtonStates[Bounce] #bool value to index
BounceButton_rect = BounceButton.get_rect(center=(width/12, height*8.09/17 + 77))

BlankBox = pygame.image.load('Images/BlankBox.png').convert_alpha() #blank boxes for top right as its only text to be rendered over it
baseBlankBox_rect = BlankBox.get_rect(center=(width-105,45))

NeedHelp = False #need help == true will show the helping menu. 
HelpButton = pygame.image.load('Images/Help.png').convert_alpha()
HelpButton_rect = HelpButton.get_rect(center=(width-60,height-60))
HelpMenu = pygame.image.load('Images/HelpMenu.png').convert_alpha()

HideButton = pygame.image.load('Images/HideUI.png').convert_alpha()
HideButton_rect = HideButton.get_rect(topleft=(0,0))
HideUI = False


#custom event for when the projectile lands. (called when the time of the current motion elapses)
landing = pygame.event.custom_type()

#custom event for when zoomed in or out, to multiply coordinates by the scale variable
scaleshift = pygame.event.custom_type()
scaleshiftevent = pygame.event.Event(scaleshift)

#custom event for if drawmode is enabled and three point parabola needs to run.
GetParabola = pygame.event.custom_type()
GetParabolaEvent = pygame.event.Event(GetParabola)


showMousePos = False
simulating = False #projectile not in motion
landed = False #projectile not landed
originstate = False #origin state is basically a ready to fire state, its to differentiate if the projectile is not in motion but its still active and not ready to fire to the projectile not being in motion and being in a ready to fire state
boolListValues = [0,0] #list for the inputs to be ready. if no inputs have been entered [0,0], if box 1 has been enter [1,0], box 1 and box 2 [1,1] so on.
path = [] #list for points of the motion with scale applied
rawpath = [] #raw list of the points without scale applied so the points can be changed upon the scaleshiftevent
initials = [initial] #list of initials
ranges = [] #list of each range of seperate motion
rawranges = [] #list of each range of seperate motion in cartesian form
RawRangeOutliers = {}


totalT = 0 #total time of the current motion
displayTimeValue = 0 #true total time value of entire motion to be displayed to user in the top right
bounceCount = 0
maxCount = 0 #counter for maximum points of motions

fakeinitial = initial #called fakeinitial as it is using the format of the initial (tuple). and it being the values for box 1 and box 2. but it cannot be the initial as when both values are confirmed for fake initial, as they are mag and angle. they need to be converted into I and J coordinates.

def currentpoint(initial, deltaTime, gravity): #function to give any coordinate of a motion at any time.
    t = deltaTime/1000    
    x = (initial[0]*t)
    y = ( (initial[1]*t) - (gravity/2)*(t**2) )
    return (x,y)

class Motion:
    def __init__(self, initial, origin, range, maxh, totaltime, gravity, motionNo):
        self.initial = initial
        self.initialx = self.initial[0]
        self.initialy = self.initial[1]
        self.range = range
        self.origin = origin
        self.originx = self.origin[0]
        self.totalT = totaltime
        self.gravity = gravity
        self.motionNo = motionNo
        self.maxheight = maxh
        
    def getpoint(self, deltaTime):
        deltaTime = deltaTime/1000
        x = (self.initialx*deltaTime)
        y = (self.initialy*deltaTime) - (self.gravity/2)*(deltaTime**2)
        return [(x,y), self.range, self.motionNo]

def hover(p, dp): #function to take in the real position of a point and its position relative to the origin and the motion, then render those in a font to be displayed when hovering over them
    return (font.render(str((round(dp[0]/scale,2),round(dp[1]/scale,2)))+'m', True,(68,71,187)), p)
            
points_rects = [] #list of rects of maximum points
originpoints_rects = [] #list of rects of originpoints
origins = [] #x values for origin points in real coordinate form ....... attempting to change it to point  values
Neworigins = []
motions = [] #list of classes of motions
origin = (width/8, height*7/8) #True Origin point
raworigins = [origin]

#initialising values for top right
displayTime = font.render(f'{round(displayTimeValue/1000,1)}s', True, (255,255,255)) #here twice to be initialised
displayTime_rect = displayTime.get_rect()
displayTime_rect.center = baseBlankBox_rect.center

displayXrange = font.render(f'{round((displayTimeValue/1000)*savedinitial[0],1)}m', True, (255,255,255))
displayXrange_rect = displayXrange.get_rect()
displayXrange_rect.center = (baseBlankBox_rect.center[0],baseBlankBox_rect.center[1]+77)

displayBounceCount = font.render(f'Bounces: {bounceCount}' , True, (255,255,255))
displayBounceCount_rect = displayBounceCount.get_rect()
displayBounceCount_rect.center = (baseBlankBox_rect.center[0],baseBlankBox_rect.center[1]+154)



displayfinal = False #bool value to show the final point
hoveringMax = False #if hovering over a maximum point
hoveringOrigin = False #if hovering over an origin point



DrawMode = True
drawing = False
incomingCollision = False
pointa = (0,0)
pointb = (0,0)
CollidingPoints = []

def ToleranceCheck(x,y):
    Tolerance = 0.005
    difference = abs(x-y)
    if difference > Tolerance:
        return True
    else:
        return False

def QuadraticSolver(a,b,c):
    discriminant = (b**2) - (4*a*c)
    if discriminant < 0:
        return 'Not Real'
    elif discriminant == 0:
        return ( -(b) + math.sqrt((b**2) - (4*a*c) ) ) / (2 * a)
    elif discriminant > 0:
        value1 = ( -(b) + math.sqrt((b**2) - (4*a*c) ) ) / (2 * a)
        value2 = ( -(b) - math.sqrt((b**2) - (4*a*c) ) ) / (2 * a)
        return [value1,value2]

linesList = []
maxpoints = []
class Line:
    def __init__(self, pointA, pointB):
        #pointA and B are in cartesian form,
        self.pointA = pointA
        self.pointB = pointB
        linesList.append(self)
        #the identities of a line should only exist for the best way to check intersection of parabola and a line, remove accordingly
        try:
            self.slope = (self.pointB[1]-self.pointA[1]) / (self.pointB[0]-self.pointA[0])
        except ZeroDivisionError:
            self.slope = float('inf')
        self.yIntercept = self.pointA[1] - (self.slope * self.pointA[0])
        
        self.angle = (math.atan(self.slope))


    def collisionCheck(self, Coefficients, origin): #coefficients of current motion.
        # if self.slope == ('inf'):
        '''the test line would ba x=13{3<y<9} now make an equasion hat gets intersectionyvalues and checks the range of them, or maybe check if x=13 is present in parabola and then check is f(13) inside the y range'''
        intersectionXValues = QuadraticSolver(Coefficients[0], Coefficients[1] - self.slope, Coefficients[2] - self.yIntercept)
        Restriction = sorted([self.pointA[0],self.pointB[0]])
        
        if type(intersectionXValues) == list:
            intersectionXValues_valid = []
            for xVal in intersectionXValues:
                if xVal >= Restriction[0] and xVal <= Restriction[1]:
                    intersectionXValues_valid.append(xVal)

            for xVal in intersectionXValues_valid:
                if ToleranceCheck(origin[0], xVal):
                    return xVal

        elif type(intersectionXValues) == float:
            if intersectionXValues >= Restriction[0] and intersectionXValues <= Restriction[1]:
                return intersectionXValues
        else:
            return False
    
    def YValueFromXValue(self, X):
        return (self.slope*(X-self.pointA[0]) + self.pointA[1])


#Origin should be in cart form
def timeToReachX(initial, X, currentOrigin):
    return (X-currentOrigin[0]) / (initial[0])

# Line( (38,1), (44,2.5) )
# Line( (20,2), (30,8))
# Line( (-2,2), (8,4))
# Line( (10,2), (50,16))
Line( (13,3), (13,9))
# def YValueFromX(initial): 
#     return ((initial[1]*X)/initial[0]) + (-g/2)*((X**2)/(initial[0]**2))

def threepointparabola(x1,y1,x2,y2,x3,y3):
    #they should all be cartesian form
    #function will return coeffs of quadratic equation in the form of ax2+bx+c
    # print(x1,y1,x2,y2,x3,y3)
    a = ( ((x3-x2)*(y2-y1)) - ((x2-x1)*(y3-y2)) ) / ( ((x3-x2)*(x2**2-x1**2)) - ((x2-x1)*(x3**2-x2**2)) )
    
    b = ( (y2-y1)-a*(x2**2-x1**2) ) / (x2-x1)
    
    c = y1 - a * x1**2-b*x1
    
    # print(x1,y1,x2,y2,x3,y3)
    print('coeffs= ',a,b,c)
    
    return [a,b,c]

def pixelToCart(p, CurrentXshift, CurrentYshift, CurrentScale):
    p = ( (p[0] - origin[0] + CurrentXshift)/CurrentScale, (origin[1] - p[1] - CurrentYshift)/CurrentScale )
    return p

def xrangeGivenOrigin(init, currentOrigin):
    timeValues = QuadraticSolver( ((-1/2)*g), (init[1]), (currentOrigin[1]))
    if timeValues[0] > 0:
        posTVal = timeValues[0]
    else:
        posTVal = timeValues[1]
    return (init[0]*posTVal)


teststring = ''

NextLineIndex = False
CollisionOriginPoints = {}
CollisionRawRanges = {}
RawRangeOutliers = {}
debugdots = []
NextCollisionXPoint = ''
CollidingPoints = []
rawranges = []
while running:
    pygame.event.post(scaleshiftevent) #calls the event that shifts all coordinates to the current scale
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
    '''
    If the values are entered, it displays the saved initial. and it displays it according to which mode you are in
    so if the values are entered and im in IJMode it can display the savedinitial fine, but if im in the other mode, it needs to convert them into magnitude and angle form before displaying.
    I keep the initial variable in the form I & J the entire time to make calculations simple. I only need to adjust if in angle & mag mode and displaying it to user
    '''
    
    dT = clock.get_time() #deltaTime
            
    #turning the display values of box 1 and box 2 into fonts ready to be blit
    displayBox1Text = font.render(displayValueBox1, True, (255,255,255))
    displayBox1Text_rect = displayBox1Text.get_rect()
    displayBox1Text_rect.center = Box1_rect.center
    displayBox2Text = font.render(displayValueBox2, True, (255,255,255))
    displayBox2Text_rect = displayBox2Text.get_rect()
    displayBox2Text_rect.center = Box2_rect.center
    
    
    #Information boxes of the motion in the top right, inside game loop so text can update
    displayBounceCount = font.render(f'Bounces: {bounceCount}' , True, (255,255,255)) 
    displayTime = font.render(f'{round(displayTimeValue/1000,1)}s', True, (255,255,255))
    displayXrange = font.render(f'{round((displayTimeValue/1000)*savedinitial[0],1)}m', True, (255,255,255))
    
    Restitution_text = font.render(displayRestitution, True, (255,255,255))
    Restitution_text_rect = Restitution_text.get_rect()
    Restitution_text_rect.center = (RestitutionButton_rect.center[0]+55,RestitutionButton_rect.center[1]+2)
    
    testText = font.render(str([round(x) for x in rawranges]), True, (255,255,255))
    slopeslist = [math.degrees(x.angle) for x in linesList]
    testText = debugfont.render((f'{incomingCollision} {Neworigins}'), True, (255,255,255))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningProjectile = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not HideUI and not inputting and not inputtingE: #will not attempt to detect input on rects if UI is hidden or if already inputting
            if FireButton_rect.collidepoint(event.pos):
                if not simulating and originstate: #only fires when in a ready to fire state
                    pygame.time.set_timer(landing, round(time(initial)*1000), 1)
                    motions.append(Motion(initial, origin, xrange(initial),maxheight(initial), time(initial), g, 0))
                    simulating = True
                    originstate = False
                    
                    # rawranges.append(xrange(initial))
                    # print(rawranges)
                    #initial is in cart form, xrange/maxheight functions take-in/return cart form
#                         Coeffs = threepointparabola(0,0,xrange(initial)/2, maxheight(initial), xrange(initial), 0)
                    if DrawMode:
                        pygame.event.post(GetParabolaEvent)
#                         originCartForm = pixelToCart((origin[0],origin[1]), xshift, yshift, scale)
#                         maxpointCartForm = pixelToCart((origin[0] + maxpointsx[bounceCount], 0), xshift, yshift, scale)
#                         Coeffs = threepointparabola(originCartForm[0], originCartForm[1], maxpointCartForm[0], maxheight(initial), xrange(initial), originCartForm[1])
                
                    
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
                Neworigins = []
                origin = (width/8, height*7/8)
                bounceCount = 0
                initial = savedinitial
                motions = []
                maxpoints = []
                maxCount = 0
                points_rects = []
                originpoints_rects = []
                displayfinal = False
                rawranges = []
                CollisionOriginPoints = {}
                RawRangeOutliers = {}
                linesList = []

                
            if ShowTrailButton_rect.collidepoint(event.pos):
                showtrail = not showtrail #swaps bool value
                ShowTrailButton = ShowTrailButton_States[showtrail] #bool value for index
            
            if Box1_rect.collidepoint(event.pos):
                if originstate or not all(boolListValues): #if in ready state to be fired or if not all values have been entered, as values can not be entered and will not be in a ready to fire state
                    Inputter = InputterStates[1]
                    inputting = True
                    selected = 0 #box 1
                    displayWorkingValue = ''#when inputting it displays nothing by default because nothing has been typed
                    
            if Box2_rect.collidepoint(event.pos):
                if originstate or not all(boolListValues): ##^
                    Inputter = InputterStates[2]
                    inputting = True
                    selected = 1 #box 2
                    displayWorkingValue = '' ##^
                    
            if SwitchButton_rect.collidepoint(event.pos):
                if originstate or not all(boolListValues):
                    IJmode = not IJmode #reverses bool value
                    Overlay = OverlayStates[IJmode] #bool value for index
                    boolListValues = [0,0] #empties to values when switching mode therefore values are not ready
                    originstate = False #not in a ready to fire state as the values have just been emptied
                    displayValueBox1 = '' #when inputting displays nothing as nothing has been typed
                    displayValueBox2 = ''
                
            if BounceButton_rect.collidepoint(event.pos):
                Bounce = not Bounce #reverses bool value
                
            if RestitutionButton_rect.collidepoint(event.pos):
                if originstate or not all(boolListValues):
                    inputtingE = True
                    workingRestitution = '' #when inputting displays nothing as nothing has been typed
            
            if drawing:
                if event.pos[1] > (height*7/8):
                    drawing = False
                else:
                    drawingPointA = event.pos
        
        if event.type == pygame.MOUSEBUTTONUP and not HideUI and not inputting and not inputtingE:
            if drawing:
                if event.pos[1] < (height*7/8):
                    drawingPointB = event.pos
                    
                    #converting from raw pixel coordinate to cartesian form (scaled coordinate system the projectile uses)
                    drawingPointA = ( (drawingPointA[0] - origin[0] + xshift)/scale, (origin[1] - drawingPointA[1] - yshift)/scale )
                    drawingPointB = ( (drawingPointB[0] - origin[0] + xshift)/scale, (origin[1] - drawingPointB[1] - yshift)/scale )
                    
                    Line(drawingPointA, drawingPointB)
                drawing = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if HideButton_rect.collidepoint(event.pos):
                HideUI = not HideUI #swaps bool
                
        if event.type == pygame.KEYDOWN:
            if inputting: 
                if event.key >= 48 and event.key <= 57: #48-57 is the relative key for digits 0-9, if inputting it detects if a key from 0-9 has been inputted and it adds it to emptystring, backspace and period is also allowed
                    displayWorkingValue = displayWorkingValue + str(pygame.key.name(event.key))
                if event.key == pygame.K_PERIOD:
                    displayWorkingValue = displayWorkingValue + str(pygame.key.name(event.key))
                if event.key == pygame.K_BACKSPACE:
                    displayWorkingValue = displayWorkingValue[:-1] #deletes last value of str
                if event.key == pygame.K_RETURN and not not displayWorkingValue.strip('0') and displayWorkingValue.count('.') <= 1: #(not str) returns True if the str is empty therefore (not not str) returns False if the str is empty, stripping the 0 so if the inputted value is only 0 and it is stripped the len() will then be 0. making sure only one period is entered
                    if IJmode:
                        if selected == 0: #box 1
                            try:
                                initial = ( int(displayWorkingValue), initial[1] ) 
                            except:
                                initial = ( float(displayWorkingValue), initial[1] )
                        
                        if selected == 1:
                            try:
                                initial = ( initial[0], int(displayWorkingValue) ) 
                            except:
                                initial = ( initial[0], float(displayWorkingValue) )
                        #try: int(new value) because if its an integer a display of x.0 is unnecasary and can just be displayed as x, if must be a float then it will be displayed x.y        
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
                        #does everything the same as IJmode but under a different variable, fakeinitial.
                        initial = ( round(fakeinitial[0]*math.cos(math.radians(fakeinitial[1])),2), round(fakeinitial[0]*math.sin(math.radians(fakeinitial[1])),2))#now we declare initial with fakeinitial being converted from mag & angle to I & J
                    savedinitial = initial #because the value has been confirmed the new constant displayed value needs to be redeclared. stated above why a savedinitial variable exists
                    initials = [savedinitial]
                    boolListValues[selected] = 1 #selected is a 0 or 1 for which box. therefore can be used to index the boollistvalues and declare that this value is ready
                    inputting = False
                    if all(boolListValues): #if all values are ready it is in a ready to fire state
                        originstate = True
                
            if inputtingE:
                if event.key >= 48 and event.key <= 57: #getting keys from 0-9, slash is also allowed
                    workingRestitution = workingRestitution + str(pygame.key.name(event.key))
                if event.key == pygame.K_SLASH:
                    workingRestitution = workingRestitution + str(pygame.key.name(event.key))
                if event.key == pygame.K_BACKSPACE:
                    workingRestitution = workingRestitution[:-1] #deletes last value of str
                if event.key == pygame.K_RETURN and len(workingRestitution.strip('/')) >= 3 and '/' in workingRestitution.strip('/') and workingRestitution.count('/') == 1 and len(workingRestitution.strip('0')) >= 3: #the length of the string must be 3 and we must strip '/'s before checking the length. we must also check that '/' is in the str after '/' is stripped  and that the count of '/' is only 1. we must also check the length of str when '0' is stripped as we cannot have 'x/0' or '0/x'
                    inputtingE = False 
                    a = int(workingRestitution[:workingRestitution.find('/')]) #grabbing the a from this str
                    b = int(workingRestitution[workingRestitution.find('/')+1:]) #grabbing the b from this str
                    e = a/b #declaring restitution value
                    
            if event.key == pygame.K_ESCAPE:
                running = False #ends game loop
                
            if event.key == pygame.K_UP:
                yshift -= 20
                
            if event.key == pygame.K_DOWN:
                if yshift != 0: #limits the yshift so it cannot go more down then needed
                    yshift += 20
                    
            if event.key == pygame.K_RIGHT:
                xshift += 20
                
            if event.key == pygame.K_LEFT:
                if xshift != 0: #limits the xshift so it cannot go more left then needed
                    xshift -= 20
                
            if event.key == pygame.K_i:
                scale += 0.25
                
            if event.key == pygame.K_o:
                if scale != 0.25: #limiting scale as scale equalling 0 causes errors
                    scale -= 0.25
            
            if event.key == pygame.K_m:
                showMousePos = not showMousePos #swap bool
                
            if event.key == pygame.K_r: #resets offset and scale
                xshift, yshift = 0,0
                scale = 20
            #inputs to be turned into buttons
            if event.key == pygame.K_d:
                drawing = True
            if event.key == pygame.K_f:
                DrawMode = not DrawMode
            if event.key == pygame.K_j:
                pygame.time.set_timer(landing, 1, 1)

        if event.type == scaleshift: #event called to adjust the coordinate points to the required scale
            # ranges = [scale*xrange(init) for init in initials] #updates list of ranges for every initial
            rawranges = [xrange(init) for init in initials]
            
            # maxheights = [scale*maxheight(init) for init in initials] #updates list of maxheights for every initial
            

            # origins = [] #resets the origin list as it needs to be updated according to the range of each motion to adjust for scale
            # for i,r in enumerate(ranges):
            #     if i == 0: 
            #         origins.append(r) #the first origin (other then true origin) will be exactly the range of first initial
            #     else:
            #         origins.append(origins[i-1]+r) #any origin after that is the origin before it + the range because the origin befaur is the sum of the ranges, so I take the sum of ranges and add on the current range

            if RawRangeOutliers:
                for index, RealRange in RawRangeOutliers.items():
                    rawranges[index] = RealRange

            ranges = [scale*r for r in rawranges]

            Neworigins = []
            for i,r in enumerate(ranges):
                if i == 0:
                    Neworigins.append((r,0))
                else:
                    
                    Neworigins.append((Neworigins[i-1][0]+r,0))


            ####

            rawmaxpointsx = []
            for i,r in enumerate(rawranges):
                if i == 0:
                    rawmaxpointsx.append(rawranges[i]/2) #first maxpoint will be half the first range
                else:
                    rawmaxpointsx.append(sum(rawranges[:i])+rawranges[i]/2) #any maxheight after this will be the sum of the ranges up to the origin just before this maximum point. then adding half of the current range/2 to get in the middle.
            maxpointsx = [scale*xdistance for xdistance in rawmaxpointsx]


            Neworigins.insert(0,(0,0))
            if CollisionOriginPoints:
                for i, o in CollisionOriginPoints.items():
                    Neworigins[i] = (scale*o[0],scale*o[1])
            
            

            Neworigins = [ ( (o[0]+(width/8), (height*7/8)-o[1]) ) for o in Neworigins]

            if incomingCollision:
                currentOriginCartForm = pixelToCart(Neworigins[bounceCount],xshift,yshift,scale)
                RawRangeOutliers[bounceCount] = NextCollisionXPoint - currentOriginCartForm[0]
                # print(f'RawRangeOutliers[{bounceCount}] = {RawRangeOutliers[bounceCount]}, because {NextCollisionXPoint} - {currentOriginCartForm[0]}, {Neworigins[bounceCount+1]}')
                CollisionOriginPoints[bounceCount+1] = (NextCollisionXPoint, NextCollisionYPoint)
            

            maxpoints = [(scale*xrange(init)/2 + Neworigins[i][0] - xshift, Neworigins[i][1] - scale*maxheight(init)- yshift) for i,init in enumerate(initials)] #updates list of maxheights for every initial

            #Creating rects for all of these vital points so they can have hover detection to know if their coordinates should be displayed or not
            # points_rects = []
            # for i in range(len(maxpointsx)):
            #     temprect = pygame.Rect(0,0,10,10)
            #     temprect.center = (width/8 + maxpointsx[i] - xshift,height*7/8 - maxheights[i] - yshift)
            #     points_rects.append(temprect)
            points_rects = []
            for i in range(len(maxpoints)):
                temprect = pygame.Rect(0,0,10,10)
                temprect.center = maxpoints[i]
                points_rects.append(temprect)


            originpoints_rects = []
            for i in range(len(Neworigins)):
                temprect = pygame.Rect(0,0,10,10)
                temprect.center = (Neworigins[i][0]-xshift,Neworigins[i][1]-yshift)
                originpoints_rects.append(temprect)

            temprect = pygame.Rect(0,0,10,10)
            if incomingCollision:
                temprect.center = (origin[0] + scale*NextCollisionXPoint-xshift,origin[1] - scale*NextCollisionYPoint - yshift)
                finalpoint_rect = temprect
            else:
                temprect.center = (origin[0] + sum(ranges) - xshift, origin[1] - yshift)#im too lazy to correct this rn so do it pretty please 🥺
                finalpoint_rect = temprect

            
            path = [[(scale*p[0][0],scale*p[0][1]),(p[1]), p[2]] for i,p in enumerate(rawpath)] #this is taken from the getpoint function in the motion class,the points are multiplied by the scale as it can be constantly changed index 1 is unused can be ignored. index 2 is the motion number label. not scale dependant but used so when drawing each circle it knows what origin it is relative to as there is a list of origins
            
#and simulating was in this
        if event.type == GetParabola and len(rawranges) != 0:
            print('getting parabola🥺')
            originCartForm = pixelToCart((Neworigins[bounceCount][0],Neworigins[bounceCount][1]), xshift, yshift, scale)
            finalxPointCoeff = (originCartForm[0] + xrange(initial))
            maxpointxCoeff = ( (originCartForm[0] + finalxPointCoeff) / 2)
            Coeffs = threepointparabola(originCartForm[0], originCartForm[1], maxpointxCoeff, originCartForm[1] + maxheight(initial), finalxPointCoeff, originCartForm[1])
            CollidingPoints = []
            for i,line in enumerate(linesList):
                lineCollisionPoint = line.collisionCheck(Coeffs, originCartForm)
                # if lineCollisionPoint:
                #     Tolerance = 0.005
                #     difference = abs(originCartForm[0] - lineCollisionPoint)
                #     # print('difference', difference)
                #     # print(originCartForm[0], lineCollisionPoint)
                #     print(f'difference = {difference}, tolerance = {Tolerance}, collision = {lineCollisionPoint}, origin x point = {originCartForm[0]}, collidingpoints = {CollidingPoints}')
                #     if difference > Tolerance:
                #         print('collision detected')
                #         CollidingPoints.append(lineCollisionPoint)
                #         NextLineIndex = i
                if lineCollisionPoint:
                    #hopefully when i did the thing like only giving the value that passes tolernace it doesnt make the point detection bad yk.
                    CollidingPoints.append(lineCollisionPoint)
                    NextLineIndex = i
            # print(f'bounceCount {bounceCount}, {CollidingPoints}')
            CollidingPoints = sorted(CollidingPoints)
            if len(CollidingPoints) != 0:
                # print('collision')
                incomingCollision = True
                NextCollisionXPoint = CollidingPoints[0]
                pygame.time.set_timer(landing, round(timeToReachX(initial,NextCollisionXPoint,originCartForm)*1000), 1)
                print(f'timer for {round(timeToReachX(initial,NextCollisionXPoint,originCartForm)*1000)} ms has begun, {initial} and {NextCollisionXPoint}')
                NextCollisionYPoint = linesList[NextLineIndex].YValueFromXValue(NextCollisionXPoint)
                # print('Hit Point', NextCollisionXPoint, NextCollisionYPoint)
            else:
                incomingCollision = False

        if event.type == landing and simulating:
            print('landing')
            # print(Neworigins[bounceCount+1])
            if Neworigins[bounceCount][1] != height*7/8 and not incomingCollision:
                currentOriginCartForm = pixelToCart(Neworigins[bounceCount],xshift, yshift, scale)
                RawRangeOutliers[bounceCount] = xrangeGivenOrigin(initial,currentOriginCartForm)
                # print(f'Im a genius computer and I think that range {bounceCount} should actually be {RawRangeOutliers[bounceCount]}, because im using {initial} and origin = {currentOriginCartForm}')
            CollidingPoints = [] #clearing list for new motion to calc new ones
            if not Bounce: #if bounce is disabled and the time has elapsed then simulating must become False.
                simulating = False
                landed = True
            else:
                # if incomingCollision:
                #     theta = math.atan(linesList[NextLineIndex].slope)
                #     originCartForm = pixelToCart(Neworigins[bounceCount],xshift,yshift,scale)
                #     print(f'theta is {theta}, e={e}, initial={initial}, slope = {linesList[NextLineIndex].slope}')
                #     if (initial[1] - (g * timeToReachX(initial, NextCollisionXPoint, originCartForm))) < 0: #before maxpoint does not reflect in x axis, after maxpoint it does
                #         initial = ((-e) * (math.sin(theta)) * initial[0], (-e) * (math.cos(theta)) * (initial[1] - (g * timeToReachX(initial, NextCollisionXPoint, originCartForm))))
                #     else:
                #         initial = ((e) * (math.sin(theta)) * initial[0], (-e) * (math.cos(theta)) * (initial[1] - (g * timeToReachX(initial, NextCollisionXPoint, originCartForm))))
                reversesign = False
                # if incomingCollision:
                #     SlopeOfSurface = linesList[NextLineIndex].angle
                #     originCartForm = pixelToCart(Neworigins[bounceCount],xshift,yshift,scale)

                #     FinalVelocity = (initial[0], initial[1] - (g * timeToReachX(initial, NextCollisionXPoint, originCartForm)))
                #     FinalVelocity_direction = math.atan2(FinalVelocity[1],FinalVelocity[0])
                #     if FinalVelocity_direction < 0:
                #         FinalVelocity_direction = math.pi + FinalVelocity_direction
                    
                #     AngleIncidence = FinalVelocity_direction - SlopeOfSurface
                #     AngleReflect = AngleIncidence
                    
                #     FinalVelocity_magnitude = math.sqrt(FinalVelocity[0]**2 + FinalVelocity[1]**2)

                #     # if NextCollisionXPoint < originCartForm[0] + xrange(initial)/2 and math.degrees(SlopeOfSurface) < 90:
                #     #     NewVelocity_magnitude = (-e*FinalVelocity_magnitude)
                #     #     print('reflecting')
                #     # elif not NextCollisionXPoint < originCartForm[0] + xrange(initial)/2 and math.degrees(SlopeOfSurface) > 90:
                #     # else:
                #     #     NewVelocity_magnitude = (e*FinalVelocity_magnitude)
                #     #     print('not reflecting')
                #     ReverseYVelSign = False
                #     ReverseXVelSign = False
                #     a = Coeffs[0]
                #     b = Coeffs[1]
                #     TangentSlope = (2*a*NextCollisionXPoint+b)

                #     if NextCollisionXPoint < originCartForm[0] + xrange(initial)/2:
                #         if math.degrees(SlopeOfSurface) < 90:
                #             NewVelocity_magnitude = (-e*FinalVelocity_magnitude) #should be - if it hits the topside, bottom of it causes errors i think if it hits the bottom it should not have the minus there and the y vel should be reversed post. i dont think so anymore i think it should be reverse x direction if it hits underside
                #             if linesList[NextLineIndex].slope < TangentSlope:
                #                 ReverseXVelSign = True
                #         else:
                #             NewVelocity_magnitude = (e*FinalVelocity_magnitude) #DEFINTELY THIS
                #     else: # if it hits in second half of motion
                #         if math.degrees(SlopeOfSurface) < 90:
                #             # NewVelocity_magnitude = (e*FinalVelocity_magnitude) #DEFINTELY THIS
                #             NewVelocity_magnitude = (-e*FinalVelocity_magnitude) #should be - if it hits the topside, bottom of it causes errors i think if it hits the bottom it should not have the minus there and the y vel should be reversed post. i dont think so anymore i think it should be reverse x direction if it hits underside
                #             if linesList[NextLineIndex].slope < TangentSlope:
                #                 ReverseXVelSign = True
                #         else:
                #             NewVelocity_magnitude = (e*FinalVelocity_magnitude) # should not have - and y vel should be flipped post, 
                #             ReverseYVelSign = True
                #             if linesList[NextLineIndex].slope < TangentSlope:
                #                 ReverseXVelSign = True
                #     NewVelocity_direction = AngleReflect

                #     if ReverseYVelSign and ReverseXVelSign:
                #         initial = (-NewVelocity_magnitude*math.cos((NewVelocity_direction)),-NewVelocity_magnitude*math.sin((NewVelocity_direction)))
                #         # initial = (NewVelocity_magnitude*math.cos((FinalVelocity_direction)),-NewVelocity_magnitude*math.sin((FinalVelocity_direction)))
                #     elif ReverseXVelSign:
                #         initial = (-NewVelocity_magnitude*math.cos((NewVelocity_direction)),NewVelocity_magnitude*math.sin((NewVelocity_direction)))
                #     elif ReverseYVelSign:
                #         initial = (NewVelocity_magnitude*math.cos((NewVelocity_direction)),-NewVelocity_magnitude*math.sin((NewVelocity_direction)))
                #     else:
                #         initial = (NewVelocity_magnitude*math.cos((NewVelocity_direction)),NewVelocity_magnitude*math.sin((NewVelocity_direction)))

                #     print(initial)
                #     print(f'{math.degrees(AngleIncidence)} is the angle of incidence, {math.degrees(FinalVelocity_direction)}, {math.degrees(SlopeOfSurface)}')
                if incomingCollision:
                    SlopeOfSurface = math.degrees(linesList[NextLineIndex].angle)
                    originCartForm = pixelToCart(Neworigins[bounceCount],xshift,yshift,scale)
                    FinalVelocity = (initial[0], initial[1] - (g * timeToReachX(initial, NextCollisionXPoint, originCartForm)))
                    initial = (e*FinalVelocity[0],e*FinalVelocity[1])
                    magnitude = math.sqrt(initial[0]**2 + initial[1]**2)
                    direction = abs(math.degrees(math.atan2(initial[1],initial[0])))
                    teststring = f'{SlopeOfSurface}'
                    
                    a = Coeffs[0]
                    b = Coeffs[1]
                    TangentSlope = (2*a*NextCollisionXPoint+b)

                    if linesList[NextLineIndex].slope < TangentSlope and initial[0] > 0:
                        newdirection = direction - (direction - SlopeOfSurface) - (direction - SlopeOfSurface)
                        # print('using the other formula 😡', bounceCount)
                    else:
                        newdirection = direction + 2*SlopeOfSurface
                    initial = (magnitude*math.cos(math.radians(newdirection)),magnitude*math.sin(math.radians(newdirection)))
                else:
                    CartFormOrigin = pixelToCart(Neworigins[bounceCount], xshift, yshift, scale)
                    tValues = QuadraticSolver( ((-1/2)*g), (initial[1]), (CartFormOrigin[1]))
                    if tValues[0] > 0:
                        posTVal = tValues[0]
                    else:
                        posTVal = tValues[1]
                    FinalYVel = initial[1] - (g * posTVal)
                    initial = (initial[0], (-e)*FinalYVel)
                '''
                applies restituion to the velocity when particle hits the floor,
                it can be applied to the initial as the motion is on a horizontal plane,
                so the final velocity is always (initial[0], -initial[1]) because its a perfectly mirrored motion,
                knowing this lets me not use the formula '-e = v/u' and the need to go through the trouble of solving for final velocity
                allowing me to simply multiply the (initial[1] * e)
                '''

                incomingCollision = False

                if abs(initial[1]) < 1:
                    #caps the y-value. When the Y-velocity is uncapped because its being reduced by a fraction therefore it can never reach 0. therefore infinite bounces.
                    #this only happens in this simulation as it cannot truly account for every acting force on a real particle
                    simulating = False
                    landed = True
                else:
                    bounceCount += 1
                    CartFormOrigin = pixelToCart(Neworigins[bounceCount], xshift, yshift, scale)
                    tValues = QuadraticSolver( ((-1/2)*g), (initial[1]), (CartFormOrigin[1]))
                    if tValues[0] > 0:
                        posTVal = tValues[0]
                    else:
                        posTVal = tValues[1]

                    pygame.time.set_timer(landing, round(posTVal*1000),1)
                    # pygame.time.set_timer(landing, round(time(initial)*1000), 1) #starts a new timer of the time of the new motion with its new velocity
                    initials.append(initial) #appends the new initial velocity to the list
                    rawranges.append(xrange(initial))
                
                # motions.append(Motion(initial, (0,0), xrange(initial),maxheight(initial), time(initial), g, bounceCount)) 
                motions.append(Motion(initial, Neworigins[bounceCount], xrange(initial),maxheight(initial), time(initial), g, bounceCount))                 
            
                totalT = 0 #resets the time to be used for new motion
                
                if DrawMode:
                    pygame.event.post(GetParabolaEvent)

    screen.fill("black") #background
    if DrawMode:
        for line in linesList:
            pygame.draw.aaline(screen, 'white', (width/8 + scale*line.pointA[0] - xshift, height*7/8 - scale*line.pointA[1] - yshift), (width/8 + scale*line.pointB[0] - xshift, height*7/8 - scale*line.pointB[1] - yshift))
    ground = pygame.Rect(0 , (height*7/8) - yshift ,width,height/8)
    pygame.draw.rect(screen, 'dark green', ground) #ground
    
    for x in range(100):
        pygame.draw.circle(screen, 'blue', (width/8 + x*scale -xshift, (height*7/8) - yshift), 3)#Blue points, (placed exactly 1m apart)
            
    if HelpButton_rect.collidepoint(pygame.mouse.get_pos()):
        NeedHelp = True #if needhelp true help menu is shown
    else:
        NeedHelp = False
    
    if simulating:
        totalT += dT #totalT is the total time of the current motion. deltaTime must be added every update in the game loop
        displayTimeValue += dT #dt must be added to the displayTimeValue as displayTimeValue is the entire collected time of all motions
        path.append(motions[bounceCount].getpoint(totalT)) #appending the points to the path
        rawpath.append(motions[bounceCount].getpoint(totalT)) #rawpath exists as it is unscaled and when the scale event is called. it does not repeadetly rescale the path as that would not work. it needs to multiply the scale by the raw value
        if totalT >= (time(initial)*1000/2) and maxCount == bounceCount: #if half of the time of the current motion elapses, the maxcount should go up.
            maxCount += 1
        
    if not originstate: 
        if FireButton_rect.collidepoint(pygame.mouse.get_pos()): #Checking if hovering over the button,
            FireButton = FireButtonStates[2] #changes the state of the button to visually diplay to user it cannot currently be pressed
        else:
            FireButton = FireButtonStates[1]
            
    if inputting:#while inputting the box should display the working value. the value as its being typed
        if selected == 0:
            displayValueBox1 = displayWorkingValue
        else:
            displayValueBox2 = displayWorkingValue
    
    if inputtingE:#same as above
        displayRestitution = workingRestitution

    if landed:
        # origins.append(sum(ranges)/scale) #i think culprit of error mentioned at top but im rly busy
        # Neworigins.append( (sum(ranges),origin[1]) )
        displayfinal = True
        
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
                pygame.draw.circle(screen, 'white', (Neworigins[p[2]][0] + p[0][0] - xshift,Neworigins[p[2]][1] - p[0][1] - yshift), 3)
                # pygame.draw.circle(screen, 'white', (Neworigins[p[2]][0] + p[0][0] - xshift,Neworigins[p[2]][1] - p[0][1] - yshift), 3)

            for i in range(len(ranges)): #iterates through ranges calculated. if the index is below the maxcount display all maxpoints. same for bounceCount and origins
                if i < maxCount:
                    # pygame.draw.circle(screen, 'green', (width/8 + maxpointsx[i] - xshift, height*7/8 - maxheights[i] - yshift) , 5)
                    pygame.draw.circle(screen, 'green', maxpoints[i] , 5)

                if i <= bounceCount:
                    pygame.draw.circle(screen, 'blue', (Neworigins[i][0]-xshift,Neworigins[i][1]-yshift), 5)
                    # pygame.draw.circle(screen, 'red', (Neworigins[i][0]-xshift,Neworigins[i][1]-yshift), 5)

            if displayfinal:
                pygame.draw.circle(screen, 'brown', finalpoint_rect.center, 5)

        if not showtrail and totalT < (time(initial)*1000):
            '''
            if not showing trail, the entire path does not need to be kept track of, so I can just calculate the point at the exact current time,
            indexing origins with the bounceCount as the bounceCount cannot go down as I wouldnt need to render any past motions.
            '''
            currentpos = currentpoint(initial, totalT, g)
            pygame.draw.circle(screen, 'white', (Neworigins[bounceCount][0] + currentpos[0]*scale - xshift,Neworigins[bounceCount][1] - currentpos[1]*scale - yshift), 3)
            # pygame.draw.circle(screen, 'white', (Neworigins[bounceCount][0] +  currentpos[0]*scale - xshift,Neworigins[bounceCount][1] - currentpos[1]*scale - yshift), 3)


    pygame.draw.circle(screen, 'red', (origin[0]-xshift,origin[1]-yshift), 5) # True Origin

        
        
    
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
        
        
        if showMousePos:
            MouseCoords = font.render( (f'({ round( (pygame.mouse.get_pos()[0] - origin[0] + xshift)/scale,2  ) },{ round((origin[1] - pygame.mouse.get_pos()[1]-yshift)/scale,2)})m or {pygame.mouse.get_pos()}'), True, (255,255,255))
            screen.blit(MouseCoords, (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]-32))

        screen.blit(displayBox1Text, displayBox1Text_rect)
        screen.blit(displayBox2Text, displayBox2Text_rect)        
        screen.blit(BounceButtonStates[Bounce],BounceButton_rect)
        screen.blit(HelpButton,HelpButton_rect)
        
        if NeedHelp:
            screen.blit(HelpMenu,((width/5),height/12))
            
        if showtrail:
            for i,rect in enumerate(points_rects):
                if i <= maxCount: #so it only displays what the projectile has passed through
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        hoveringMax = True
                        if not hoveringOrigin:
                            maxpoint_Cart = pixelToCart(points_rects[i],xshift,yshift,scale)
                            maxpointText = font.render(f'({round(maxpoint_Cart[0],2)},{round(maxpoint_Cart[1],2)})m',True, (68,71,187))
                            screen.blit(maxpointText,(rect.center[0], rect.center[1]-45))
                    else:
                        hoveringMax = False

                        
            for i,rect in enumerate(originpoints_rects[:-1]):
                if i <= bounceCount: #so it only displays what the projectile has passed through
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        hoveringOrigin = True
                        if not hoveringMax:
                            originCartForm = pixelToCart(Neworigins[i],xshift,yshift,scale)
                            originText = font.render(f'({round(originCartForm[0],2)},{round(originCartForm[1],2)})m', True, (68,71,187))
                            screen.blit(originText,(rect.center[0], rect.center[1]-45))
                    else:
                        hoveringOrigin = False


            if displayfinal:
                if finalpoint_rect.collidepoint(pygame.mouse.get_pos()):
                    finalpoint_Cart = pixelToCart(finalpoint_rect.center, xshift, yshift, scale)
                    finalpointText = font.render(f'({round(finalpoint_Cart[0],2)},{round(finalpoint_Cart[1],2)})m', True, (68,71,187))

                    finalpoint_rect.center = (finalpoint_rect.center[0], finalpoint_rect.center[1]-45)
                    screen.blit(finalpointText, finalpoint_rect)
                    
            # if hoveringMax or hoveringOrigin:
            #     screen.blit(hoverpostext[0],(hoverpostext[1][0], hoverpostext[1][1]-45))

    screen.blit(testText,(width/6, height/2))
    screen.blit(HideButton,HideButton_rect)
    pygame.display.flip()
    clock.tick(144)  # fps limit
pygame.quit()
exit()