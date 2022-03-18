import pygame
import random

CHANGERATE = 5
BRIGHTNESS = 255
assert 0 <= BRIGHTNESS <= 255

STARTCOLOURS = [
	(BRIGHTNESS, random.randint(0,BRIGHTNESS), 0),
	(BRIGHTNESS, 0, random.randint(0,BRIGHTNESS)),
	(random.randint(0,BRIGHTNESS), BRIGHTNESS, 0),
	(0, BRIGHTNESS, random.randint(0,BRIGHTNESS)),
	(random.randint(0,BRIGHTNESS), 0, BRIGHTNESS),
	(0, random.randint(0,BRIGHTNESS), BRIGHTNESS)]

def rainbow(rgb: tuple):
    assert len(rgb) == 3 and rgb[0] == int(rgb[0]) and rgb[1] == int(rgb[1]) and rgb[2] == int(rgb[2]), "Tuple must be 3 integers"
    r, g, b = rgb
    
    if r < BRIGHTNESS and g == 0 and b == BRIGHTNESS:
    	r += CHANGERATE
    elif 0 < r <= BRIGHTNESS and g == BRIGHTNESS and b == 0:
    	r -= CHANGERATE
    elif r == BRIGHTNESS and g < BRIGHTNESS and b == 0:
    	g += CHANGERATE
    elif r == 0 and 0 < g <= BRIGHTNESS and b == BRIGHTNESS:
    	g -= CHANGERATE
    elif r == 0 and g == BRIGHTNESS and b < BRIGHTNESS:
    	b += CHANGERATE
    elif r == BRIGHTNESS and g == 0 and 0 < b <= BRIGHTNESS:
    	b -= CHANGERATE

    if r <= 0:          r = 0
    if r >= BRIGHTNESS: r = BRIGHTNESS
    if g <= 0:          g = 0
    if g >= BRIGHTNESS: g = BRIGHTNESS
    if b <= 0:          b = 0
    if b >= BRIGHTNESS: b = BRIGHTNESS

    return (r,g,b)


def main():
    FULLSCREEN = True
    pygame.init()
    info = pygame.display.Info()

    if FULLSCREEN:
        SCREENWIDTH = info.current_w
    	SCREENHEIGHT = info.current_h
    	del info
    else:
        SCREENWIDTH = 500
        SCREENHEIGHT = 500
        del info
    
    if FULLSCREEN: screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT], pygame.FULLSCREEN)
    else: screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])

    clock = pygame.time.Clock()
    colour = random.choice(STARTCOLOURS)

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
        screen.fill(colour)
        print(colour)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
