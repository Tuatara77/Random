import math
import pygame

SCREENWIDTH, SCREENHEIGHT = 900,770

WAVECOUNT = 2

EQUILIBRIUM_LINE_1_YCOORD = SCREENHEIGHT//7
EQUILIBRIUM_LINE_2_YCOORD = 3*(SCREENHEIGHT//7)
EQUILIBRIUM_LINE_3_YCOORD = 11*(SCREENHEIGHT//14)

white = (255,255,255)
black = (0,0,0)

class Point(pygame.sprite.Sprite):
    def __init__(self,x,y,vel, group):
        super().__init__()
        self.image = pygame.Surface([3,3])
        self.rect = self.image.get_rect()
        self.image.fill(white)

        self.rect.centerx = x
        self.rect.centery = y
        self.dx = vel

        group.add(self)
    
    def update(self):
        if self in progressive:
            self.rect.x -= self.dx
            if self.rect.x < 90:
                self.rect.x = SCREENWIDTH-92
            if self.rect.x > SCREENWIDTH-92:
                self.rect.x = 90

        if self in stationary:
            alist = []
            for f in progressive:
                if f.rect.centerx == self.rect.centerx:
                    alist.append(f.rect.centery)
            if len(alist) == 2:
                coord1 = EQUILIBRIUM_LINE_2_YCOORD-alist[0]
                coord2 = EQUILIBRIUM_LINE_1_YCOORD-alist[1]
                coord3 = coord1+coord2
                self.rect.centery = EQUILIBRIUM_LINE_3_YCOORD+coord3


pygame.init()
screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])

progressive = pygame.sprite.Group()
stationary = pygame.sprite.Group()
clock = pygame.time.Clock()

for f in range(int(WAVECOUNT*360)):
    Point(f+90,(2*(SCREENHEIGHT//14))-int((80*(math.sin(math.radians(f))))), 1, progressive)
    Point(f+90,(6*(SCREENHEIGHT//14))-int((80*(math.sin(math.radians(f))))), -1, progressive)
    Point(f+90,11*(SCREENHEIGHT//14), 0, stationary)

done = False
while not done:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    
    progressive.update()
    stationary.update()

    screen.fill(black)
    
    pygame.draw.line(screen, white, (90,EQUILIBRIUM_LINE_1_YCOORD), (SCREENWIDTH-92,EQUILIBRIUM_LINE_1_YCOORD), 1)
    pygame.draw.line(screen, white, (90,EQUILIBRIUM_LINE_2_YCOORD), (SCREENWIDTH-92,EQUILIBRIUM_LINE_2_YCOORD), 1)
    pygame.draw.line(screen, white, (90,EQUILIBRIUM_LINE_3_YCOORD), (SCREENWIDTH-92,EQUILIBRIUM_LINE_3_YCOORD), 1)
    
    progressive.draw(screen)
    stationary.draw(screen)
    pygame.display.flip()
pygame.quit()