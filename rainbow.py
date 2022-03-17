import pygame
import random

CHANGERATE = 1

def rainbow(rgb: tuple):
    assert len(rgb) == 3 and rgb[0] == int(rgb[0]) and rgb[1] == int(rgb[1]) and rgb[2] == int(rgb[2]), "Tuple must be 3 integers"
    r, g, b = rgb
    
    if r < 255 and g == 0 and b == 255:         r += CHANGERATE
    elif 0 < r <= 255 and g == 255 and b == 0:  r -= CHANGERATE
    elif r == 255 and g < 255 and b == 0:       g += CHANGERATE
    elif r == 0 and 0 < g <= 255 and b == 255:  g -= CHANGERATE
    elif r == 0 and g == 255 and b < 255:       b += CHANGERATE
    elif r == 255 and g == 0 and 0 < b <= 255:  b -= CHANGERATE

    if r <= 0:   r = 0
    if r >= 255: r = 255
    if g <= 0:   g = 0
    if g >= 255: g = 255
    if b <= 0:   b = 0
    if b >= 255: b = 255

    return (r,g,b)


def main():
    FULLSCREEN = False
    pygame.init()
    info = pygame.display.Info()

    if FULLSCREEN: SCREENWIDTH, SCREENHEIGHT = info.current_w, info.current_h; del info
    else: SCREENWIDTH, SCREENHEIGHT = 500,500; del info
    if FULLSCREEN: screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT], pygame.FULLSCREEN)
    else: screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])

    clock = pygame.time.Clock()
    colour = random.choice([(255,0,0), (0,255,0), (0,0,255)])

    done = False
    while not done:
        clock.tick_busy_loop(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
        
        colour = rainbow(colour)
        print(colour)
        screen.fill(colour)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()