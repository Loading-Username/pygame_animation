import pygame
import math
import random
from pygame.locals import*

# Initialize Game Engine
pygame.mixer.pre_init()
pygame.init()
pygame.mixer.init()

# Images
plane = pygame.image.load('plane.png')
bush = pygame.image.load('Tree.png')
bird = pygame.image.load('Bird.png')

# Window
SIZE = (800,600)
TITLE = "Mans Not Hot"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
GREEN = (9, 234, 28)
BLUE = (106, 162, 252)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 123, 0)
YELLOW = (255, 250, 0)
PINK = (255, 0, 144)
BROWN = (102, 66, 0)
DGREEN = (0, 150, 58)
GRAY = (71, 70, 66)
DARK_BLUE = (13, 45, 96)
SMOKE = (173, 170, 163)

# Block
loc = [380, 280]
vel = [0, 0]
speed = 5

# Functions
stormy = True
daytime = True
lights_on = False

num_clouds = 20
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

def draw_block(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.rect(screen, WHITE, [x, y, 40, 40])

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]

    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def draw_door(x, y):
    pygame.draw.rect(screen, GRAY, [x, y, 50, 100])

def draw_doorknob(x,y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 5, 5])

def draw_window(x, y):
    if lightning_timer > -1:
        pygame.draw.rect(screen, YELLOW, [x, y, 50, 75])
    else:
        pygame.draw.rect(screen, BLUE, [x, y, 50, 75])
        

def draw_raindrop(drop):
    rect = drop[:4]
    pygame.draw.ellipse(screen, DARK_BLUE, rect)

def draw_chimney(x, y):
    pygame.draw.rect(screen, BROWN, [x, y, 50, 75])


''' Make stars '''

stars = []

for i in range(200):

    x = random.randrange(0, 800)

    y = random.randrange(0, 400)

    r = random.randrange(1, 5)

    s = [x, y, r, r]

    stars.append(s)   

''' Make Rain '''
num_drops = 700
rain = []

for i in range(num_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(1, 5)
    stop = random.randrange(400, 700)
    drop = [x, y, r, r, stop]
    rain.append(drop)

lightning_timer = 0

    
# Sound Effects
pygame.mixer.music.load("rain.ogg")
thunder = pygame.mixer.Sound("thunder.ogg")
    

# Game Loop
pygame.mixer.music.play(-1)

done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel[0] = speed
            elif event.key == pygame.K_LEFT:
                vel[0] = -1 * speed
            if event.key == pygame.K_UP:
                vel[1] = -1 * speed
            elif event.key == pygame.K_DOWN:
                vel[1] = speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vel[0] = 0
            elif event.key == pygame.K_LEFT:
                vel[0] = 0
            if event.key == pygame.K_UP:
                vel[1] = 0
            elif event.key == pygame.K_DOWN:
                vel[1] = 0
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on
            if event.key == pygame.K_p:
                thunder.play()
            if event.key == pygame.K_q:
                screen.fill(YELLOW)
                
    # Game Logic
    loc[0] += vel[0]
    loc[1] += vel[1]

    for c in clouds:
        c[0] += 2

        if c[0] > 800:
            c[0] = random.randrange(-800, -100)
            c[1] = random.randrange(-50, 200)

    ''' Set Sky Color '''
    if daytime:
        sky = GRAY
    else:
        sky = BLACK


    ''' Move Rain '''
    for r in rain:
        r[0] += 1
        r[1] += 4

        if r[1] > r[4]:
            r[0] = random.randrange(-200, 1000)
            r[1] = random.randrange(-100, 0)
                
    ''' Lightning '''
    if random.randrange(0, 300) == 0:
        lightning_timer = 5
        thunder.play
    else:
        lightning_timer -= 1
        
      # Drawing Code (Describe the picture.)
    
    ''' sky '''
    if lightning_timer > 0:
        screen.fill(YELLOW)
        thunder.play()
    else:
        screen.fill(sky)

    ''' stars '''

    for s in stars:
        if not daytime:
            pygame.draw.ellipse(screen, YELLOW, s)
        else:
            pygame.draw.ellipse(screen, GRAY, s)
    

        
    ''' moon '''
    if not daytime:
        pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        post = [x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]
        pygame.draw.polygon(screen, WHITE, post)
    
    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 800, 5])

    ''' house '''
    pygame.draw.rect(screen, RED, [375, 400, 400, 400])

    ''' roof '''
    roof = [350, 400], [800, 400], [575, 275]
    pygame.draw.polygon(screen, ORANGE, roof)

    ''' Chimney ''' 
    draw_chimney(450, 300)
    
    ''' tree stump ''' 
    y = 500
    for x in range(50, 350, 100):
        trunk = [x, y], [x+30, y], [x+30, y+30], [x, y+30]
        pygame.draw.polygon(screen, BROWN, trunk)

    ''' leaves'''
    y = 500
    for x in range(50, 350, 100):
        leaves = [x+15,y-150], [x+60,y], [x-30,y] 
        pygame.draw.polygon(screen, DGREEN, leaves)

    ''' door '''
    draw_door(550, 500)
    
    ''' doorknob '''
    draw_doorknob(590, 550) 

    ''' windows '''
    draw_window(450, 450)
    draw_window(650, 450)

    ''' Rain '''
    for r in rain:
        if daytime:
            draw_raindrop(r)
        
    ''' clouds '''
    for c in clouds:
        draw_cloud(c)
    ''' Bush '''
    screen.blit(bush, (100, 500))

    ''' Plane '''
    screen.blit(plane, (600, 100))

    ''' Bird '''
    screen.blit(bird, (200, 100))
    screen.blit(bird, (150, 150))
    screen.blit(bird, (250, 150))

    # Update Screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()


