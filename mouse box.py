import pygame

screenwidth, screenheight = 800,450
boxwidth, boxheight = 100,100

red = (255,0,0)
green = (0,255,0)
black = (0,0,0)

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([boxwidth,boxheight])
        self.rect = self.image.get_rect()
        self.image.fill(red)

        self.rect.centerx = x
        self.rect.centery = y

        boxes.add(self)


pygame.init()
screen = pygame.display.set_mode([screenwidth, screenheight])

boxes = pygame.sprite.Group()

box = Box(screenwidth/2, screenheight/2)

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    
    mouse = pygame.mouse.get_pos()

    if box.rect.x <= mouse[0] <= box.rect.x + boxwidth and box.rect.y <= mouse[1] <= box.rect.y + boxheight:
        box.image.fill(green)
    else:
        box.image.fill(red)
    
    screen.fill(black)
    boxes.draw(screen)

    pygame.display.flip()
pygame.quit()