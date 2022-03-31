import pygame

FULLSCREEN = True

pointg = pygame.sprite.Group()
class Point(pygame.sprite.Sprite):
    def __init__(self, x,y,size):
        super().__init__()
        self.image = pygame.Surface([size,size])
        self.rect = self.image.get_rect()
        self.image.fill((255,255,255))

        self.rect.topleft = (x,y)
        self.velx = 1
        self.vely = 1

    def move(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        if self.rect.left < 0 or self.rect.right > SCREENWIDTH: self.velx *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREENHEIGHT: self.vely *= -1


pygame.init()

if FULLSCREEN: SCREENWIDTH, SCREENHEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
else: SCREENWIDTH, SCREENHEIGHT = 1000, 990

screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])

point = Point(0,0,1)
clock = pygame.time.Clock()

done = False
while not done:
    # clock.tick_busy_loop(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    
    point.move()

    # screen.fill((0,0,0))
    screen.blit(point.image, point.rect)
    pygame.display.flip()
pygame.quit()